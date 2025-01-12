import json
import os
from datetime import datetime
import asyncio

from fruitstand.schemas import generate_baseline_schema
from fruitstand.factories import embeddings_factory, llm_factory
from fruitstand.utils import file_utils

def start(args):
    # Open and read the input file
    with open(args.filename, 'r') as file:
        data = json.load(file)
        
    # Validate the input data against the baseline schema
    generate_baseline_schema.validate(data)

    # Extract LLM query parameters from args
    query_llm = args.query_llm
    query_api_key = args.query_api_key

    # Initialize the LLM service
    llm_service = llm_factory.getLLM(query_llm, query_api_key)
    query_model = args.query_model

    # Validate the query model
    llm_supported_model = llm_service.validate_model(query_model)
    if not llm_supported_model:
        raise TypeError(f"{args.query_model} is not a valid query model for {query_llm}")
    
    # Extract embeddings parameters from args
    embeddings_llm = args.embeddings_llm
    embeddings_api_key = args.embeddings_api_key
    
    # Initialize the embeddings service
    embeddings_service = embeddings_factory.getEmbeddings(embeddings_llm, embeddings_api_key)
    embeddings_model = args.embeddings_model

    # Validate the embeddings model
    embeddings_supported_model = embeddings_service.validate_embeddings(embeddings_model)
    if not embeddings_supported_model:
        raise TypeError(f"{args.embeddings_model} is not a valid embeddings model for {embeddings_llm}")
    
    # Generate the baseline data
    baseline_data = _generate_baseline(llm_service, query_model, embeddings_service, embeddings_model, data)

    # Output the baseline data to a file
    _output_baseline(query_llm, query_model, embeddings_llm, embeddings_model, baseline_data, args.output_directory)

def _generate_baseline(llm_service, query_model, embeddings_service, embeddings_model, data):
    baseline_data = []

    # Process each query in the input data
    for query in data:
        baseline_data.append(_run_query_baseline(llm_service, query_model, embeddings_service, embeddings_model, query))
    
    return baseline_data

def _run_query_baseline(llm_service, query_model, embeddings_service, embeddings_model, query):
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
    output_file = f"baseline__{query_llm.lower()}_{query_model.lower()}__{embeddings_llm.lower()}_{embeddings_model.lower()}__{str(datetime.now().timestamp())}.json"

    # Generate the full path for the output file
    output_full_path = os.path.join(output_directory, file_utils.str_to_safe_filename(output_file))

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