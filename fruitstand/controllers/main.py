from fruitstand.controllers import baseline, test
from typing import Any

class Args:
    filename: str
    query_llm: str
    query_api_key: str
    query_model: str
    embeddings_llm: str
    embeddings_api_key: str
    embeddings_model: str
    output_directory: str
    baseline_embeddings_api_key: str
    baseline_filename: str
    test_filename: str
    success_threshold: float

def start(command: str, args: Args) -> None:
    normalized_command = command.lower()

    if normalized_command == "baseline":
        print(args.filename)
        baseline.start_filebased(
            args.filename, 
            args.query_llm, 
            args.query_api_key, 
            args.query_model, 
            args.embeddings_llm, 
            args.embeddings_api_key, 
            args.embeddings_model,
            args.output_directory
        )
    elif normalized_command == "test":
        test.start_filebased(
            args.baseline_filename, 
            args.test_filename, 
            args.query_llm,
            args.query_api_key,
            args.query_model,
            args.baseline_embeddings_api_key,
            args.success_threshold,
            args.output_directory
        )
    else:
        raise TypeError("Unknown command: " + command)