from fruitstand.controllers import baseline, test

def start(command, args):
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
            args.embeddings_api_key,
            args.success_threshold,
            args.output_directory
        )
    else:
        raise TypeError("Unknown command: " + command)