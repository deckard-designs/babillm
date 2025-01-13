import os
import json
import asyncio
import logging
from datetime import datetime

from fruitstand.factories import embeddings_factory, llm_factory
from fruitstand.schemas import baseline_schema, test_data_schema
from fruitstand.utils import file_utils, vector_utils

def start_filebased(
    baseline_filename, 
    test_filename, 
    test_query_llm,
    test_query_api_key,
    test_query_model,
    embeddings_api_key,
    success_threshold,
    output_directory
):
    logging.info(f"Reading the existing baseline from {baseline_filename}")

    # Load and validate baseline data
    with open(baseline_filename, 'r') as file:
        baseline_data = json.load(file)

    logging.info("Validating baseline data")
    
    baseline_schema.validate(baseline_data)

    logging.info(f"Reading the test data from from {test_filename}")

    # Load and validate test data
    with open(test_filename, 'r') as file:
        test_data = json.load(file)

    test_responses = start(
        test_query_llm,
        test_query_api_key,
        test_query_model,
        embeddings_api_key,
        success_threshold,
        baseline_data,
        test_data
    )
     
    # Output test results
    output_file = _output_results(
        test_query_llm, 
        test_query_model,
        test_responses,
        output_directory
    )

    logging.info(f"Test data outputted to {output_file}")

def start(
    test_query_llm,
    test_query_api_key,
    test_query_model,
    embeddings_api_key,
    success_threshold,
    baseline_data,
    test_data
):
    logging.info("Validating test data")
    
    test_data_schema.validate(test_data)

    logging.info("Retrieving LLM and embedding libraries")

    test_responses = []

    # Initialize LLM service and validate model
    test_llm_service = llm_factory.getLLM(test_query_llm, test_query_api_key)
    llm_supported_model = test_llm_service.validate_model(test_query_model)

    if llm_supported_model == False:
        raise TypeError(f"{test_query_model} is not a valid query model for {test_query_llm}")

    # Initialize embeddings service and validate model
    embeddings_service = embeddings_factory.getEmbeddings(baseline_data["embeddings"]["source"], embeddings_api_key)
    embeddings_model = baseline_data["embeddings"]["model"]

    if llm_supported_model == False:
        raise TypeError(f"{embeddings_model} is not a valid embeddings model for {embeddings_service}")

    logging.info("Running tests against baseline data")

    logging.info(f"Success threshold: {success_threshold}")

    test_responses = asyncio.run(run_tests(
        test_llm_service, 
        test_query_model, 
        embeddings_service, 
        embeddings_model,
        baseline_data,
        test_data,
        success_threshold
    ))

    logging.info(f"Tests complete!")

    return test_responses

async def run_tests(
    test_llm_service, 
    test_query_model, 
    embeddings_service, 
    embeddings_model,
    baseline_data,
    test_data,
    success_threshold
):
    # Run tests for each query in test data
    test_results = [ _generate_test_results(
        test_llm_service, 
        test_query_model, 
        embeddings_service, 
        embeddings_model,
        baseline_data,
        query,
        success_threshold
    ) for query in test_data ]

    return await asyncio.gather(*test_results)


async def _generate_test_results(
    test_llm_service, 
    test_query_model, 
    embeddings_service, 
    embeddings_model,
    baseline_data,
    query,
    success_threshold
):
    try:
        response, similarity, status = _run_test(
            test_llm_service, 
            test_query_model, 
            embeddings_service, 
            embeddings_model,
            baseline_data,
            query,
            success_threshold
        )
    except TypeError as e:
        status = "failed"
        response = str(e)
        similarity = 0

        logging.error(f"Testing: {query}: (failed)")
    else:
        logging.info(f"Testing: {query}: (passed) {similarity} similarity")
    
    return {
        "query": query,
        "status": status,
        "response": response,
        "similarity": similarity
    }


def _run_test(test_llm_service, test_query_model, embeddings_service, embeddings_model, baseline_data, query, success_threshold):
    # Find the corresponding baseline test data
    baseline_test = _find_baseline_test(query, baseline_data["data"])

    if baseline_test != None:
        # Query the LLM service and get the response
        response = test_llm_service.query(test_query_model, query)

        # Embed the response and calculate similarity
        response_vector = embeddings_service.embed(embeddings_model, response)
        similarity = vector_utils.cosine_similarity(baseline_test["vector"], response_vector)
           
        # Determine test status based on similarity threshold
        if similarity >= success_threshold:
            test_status = "passed"
        else:
            test_status = "failed"

        return response, round(similarity, 2), test_status
    else:
        raise TypeError("Cannot locate test data within baseline")
    

def _find_baseline_test(test_query, baseline_data):
    # Search for the baseline test data that matches the query
    for data in baseline_data:
        if data["query"] == test_query:
            return data
      
    return None

def _output_results(query_llm, query_model, test_results, output_directory):
    # Generate output file name and path
    output_file = f"{query_llm.lower()}_{query_model.lower()}__{str(datetime.now().timestamp())}"
    output_full_path = os.path.join(output_directory, f"{file_utils.str_to_safe_filename(output_file)}.json")

    # Write test results to the output file
    with open(output_full_path, "w") as file:
        json.dump(test_results, file, indent=4)

    return output_full_path