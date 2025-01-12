import os
import json
from datetime import datetime

from factories import embeddings_factory, llm_factory
from schemas import baseline_schema, test_data_schema
from utils import file_utils, vector_utils

def start(args):
    with open(args.baseline_filename, 'r') as file:
        baseline_data = json.load(file)

    baseline_schema.validate(baseline_data)

    with open(args.test_filename, 'r') as file:
        test_data = json.load(file)

    test_data_schema.validate(test_data)

    test_responses = []

    test_query_llm = args.query_llm

    test_llm_service = llm_factory.getLLM(test_query_llm, args.query_api_key)
    test_query_model = args.query_model

    llm_supported_model = test_llm_service.validate_model(test_query_model)

    if llm_supported_model == False:
        raise TypeError(f"{test_query_model} is not a valid query model for {test_query_llm}")

    embeddings_service = embeddings_factory.getEmbeddings(baseline_data["embeddings"]["source"], args.embeddings_api_key)
    embeddings_model = baseline_data["embeddings"]["model"]

    if llm_supported_model == False:
        raise TypeError(f"{embeddings_model} is not a valid embeddings model for {embeddings_service}")

    for query in test_data:
        try:
            response, similarity, status = _run_test(
                test_llm_service, 
                test_query_model, 
                embeddings_service, 
                embeddings_model,
                baseline_data,
                query,
                args.success_threshold
            )
        except TypeError as e:
            test_responses.append({
                "query": query,
                "status": "failed",
                "response": e,
                "similarity": 0
            })
        else:
           test_responses.append({
                "query": query,
                "status": status,
                "response": response,
                "similarity": similarity
           })
           
    _output_results(
        test_query_llm, 
        test_query_model,
        test_responses,
        args.output_directory
    )

def _run_test(test_llm_service, test_query_model, embeddings_service, embeddings_model, baseline_data, query, success_threshold):
    baseline_test = _find_baseline_test(query, baseline_data["data"])

    if baseline_test != None:
        response = test_llm_service.query(test_query_model, query)

        response_vector = embeddings_service.embed(embeddings_model, response)

        similarity = vector_utils.cosine_similarity(baseline_test["vector"], response_vector)
           
        test_status = "passed" if similarity >= success_threshold else "failed",

        return response, round(similarity, 2), test_status
    else:
        raise TypeError("Cannot locate test data within baseline")
    

def _find_baseline_test(test_query, baseline_data):
    for data in baseline_data:
        if data["query"] == test_query:
            return data
      
    return None

def _output_results(query_llm, query_model, test_results, output_directory):
    output_file = f"{query_llm.lower()}_{query_model.lower()}__{str(datetime.now().timestamp())}.json"

    output_full_path = os.path.join(output_directory, file_utils.str_to_safe_filename(output_file))

    with open(output_full_path, "w") as file:
        json.dump(test_results, file, indent=4)