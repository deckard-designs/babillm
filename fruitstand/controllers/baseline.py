import json
import os
import asyncio
import logging
from datetime import datetime

from fruitstand.schemas import generate_baseline_schema
from fruitstand.factories import embeddings_factory, llm_factory
from fruitstand.utils import file_utils

def start_filebased(
    filename, 
    query_llm, 
    query_api_key, 
    query_model, 
    embeddings_llm, 
    embeddings_api_key, 
    embeddings_model,
    output_directory
):
    logging.info("Reading test data required for generating a baseline")

    # Open and read the input file
    with open(filename, 'r') as file:
        data = json.load(file)
        
    baseline_data = start(
        query_llm, 
        query_api_key, 
        query_model, 
        embeddings_llm, 
        embeddings_api_key, 
        embeddings_model,
        data
    )

    # Output the baseline data to a file
    output_file = _output_baseline(query_llm, query_model, embeddings_llm, embeddings_model, baseline_data, output_directory)

    logging.info(f"Baseline data outputted to {output_file}")

    
def start( 
    query_llm, 
    query_api_key, 
    query_model, 
    embeddings_llm, 
    embeddings_api_key, 
    embeddings_model,
    data
):
    logging.info("Validating test data")

    # Validate the input data against the baseline schema
    generate_baseline_schema.validate(data)

    logging.info("Retrieving LLM and embedding libraries")

    # Initialize the LLM service
    llm_service = llm_factory.getLLM(query_llm, query_api_key)

    # Validate the query model
    llm_supported_model = llm_service.validate_model(query_model)
    if not llm_supported_model:
        raise TypeError(f"{query_model} is not a valid query model for {query_llm}")
    
    # Initialize the embeddings service
    embeddings_service = embeddings_factory.getEmbeddings(embeddings_llm, embeddings_api_key)

    # Validate the embeddings model
    embeddings_supported_model = embeddings_service.validate_embeddings(embeddings_model)
    if not embeddings_supported_model:
        raise TypeError(f"{embeddings_model} is not a valid embeddings model for {embeddings_llm}")
    
    logging.info("Generating baseline data")

    # Generate the baseline data
    baseline_data = asyncio.run(_generate_baseline(llm_service, query_model, embeddings_service, embeddings_model, data))

    logging.info("Baseline generated")

    return baseline_data

async def _generate_baseline(llm_service, query_model, embeddings_service, embeddings_model, data):
    # Process each query in the input data
    baseline_data = [ _run_query_baseline(llm_service, query_model, embeddings_service, embeddings_model, query) for query in data ]
    
    return await asyncio.gather(*baseline_data)

async def _run_query_baseline(llm_service, query_model, embeddings_service, embeddings_model, query):
    # Get the LLM response for the query
    llm_response = llm_service.query(query_model, query)
    # Get the embeddings for the LLM response
    response_embeddings = embeddings_service.embed(embeddings_model, llm_response)

    # Append the query, response, and embeddings to the baseline data
    return {
        "query": query,
        "response": llm_response,
        "vector": response_embeddings
    }

def _output_baseline(query_llm, query_model, embeddings_llm, embeddings_model, baseline, output_directory):
    # Create a filename for the output file
    output_file = f"baseline__{query_llm.lower()}_{query_model.lower()}__{embeddings_llm.lower()}_{embeddings_model.lower()}__{str(datetime.now().timestamp())}"
    
    # Generate the full path for the output file
    output_full_path = os.path.join(output_directory, f"{file_utils.str_to_safe_filename(output_file)}.json")

    # Write the baseline data to the output file
    with open(output_full_path, "w") as file:
        json.dump({
            "llm": {
                "source": query_llm,
                "model": query_model
            },
            "embeddings": {
                "source": embeddings_llm,
                "model": embeddings_model
            },
            "data": baseline
        }, file, indent=4)

    return output_full_path