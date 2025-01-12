import json
import os
from datetime import datetime

from schemas import generate_baseline_schema
from factories import embeddings_factory, llm_factory
from utils import file_utils

def start(args):
    with open(args.filename, 'r') as file:
        data = json.load(file)
        
    generate_baseline_schema.validate(data)

    query_llm = args.query_llm
    query_api_key = args.query_api_key

    llm_service = llm_factory.getLLM(query_llm, query_api_key)
    query_model = args.query_model

    llm_supported_model = llm_service.validate_model(query_model)

    if llm_supported_model == False:
        raise TypeError(f"{args.query_model} is not a valid query model for {query_llm}")
    
    embeddings_llm = args.embeddings_llm
    embeddings_api_key = args.embeddings_api_key
    
    embeddings_service = embeddings_factory.getEmbeddings(embeddings_llm, embeddings_api_key)
    embeddings_model = args.embeddings_model

    embeddings_supported_model = embeddings_service.validate_embeddings(embeddings_model)

    if embeddings_supported_model == False:
        raise TypeError(f"{args.embeddings_model} is not a valid embeddings model for {embeddings_llm}")
    
    baseline_data = _generate_baseline(llm_service, query_model, embeddings_service, embeddings_model, data)

    _output_baseline(query_llm, query_model, embeddings_llm, embeddings_model, baseline_data, args.output_directory)

def _generate_baseline(llm_service, query_model, embeddings_service, embeddings_model, data):
    baseline_data = []

    for query in data:
        llm_response = llm_service.query(query_model, query)
        response_embeddings = embeddings_service.embed(embeddings_model, llm_response)

        baseline_data.append({
            "query": query,
            "response": llm_response,
            "vector": response_embeddings
        })
    
    return baseline_data

def _output_baseline(query_llm, query_model, embeddings_llm, embeddings_model, baseline, output_directory):
    output_file = f"baseline__{query_llm.lower()}_{query_model.lower()}__{embeddings_llm.lower()}_{embeddings_model.lower()}_{str(datetime.now().timestamp())}.json"

    output_full_path = os.path.join(output_directory, file_utils.str_to_safe_filename(output_file))

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