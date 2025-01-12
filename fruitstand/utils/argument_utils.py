from argparse import ArgumentParser

def getArgumentParser(command):
    parser = ArgumentParser()

    normalized_command = command.lower()

    if normalized_command == "baseline":
        parser.add_argument("-f", "--filename", dest="filename", required=True,
                            help="A file containing test data is required to generate an LLM baseline")
        parser.add_argument("-o", "--output", dest="output_directory", required=True,
                            help="An output location is required for the baseline data")
        parser.add_argument("-qllm", dest="query_llm", required=True,
                            help="An llm is required that you would like to generate a baseline queries for")
        parser.add_argument("-qm", '--model', dest="query_model", required=True,
                            help="The model that for the llm that you would like to generate a baseline queries for")
        parser.add_argument("-qkey", dest="query_api_key", required=True,
                            help="The api key for the llm you would like to use for querying")
        parser.add_argument("-ellm", dest="embeddings_llm", required=True,
                            help="An llm is required that you would like to use to generate embeddings")
        parser.add_argument("-em", dest="embeddings_model", required=True,
                            help="An model is required that you would like to use to generate embeddings")
        parser.add_argument("-ekey", dest="embeddings_api_key", required=True,
                            help="The api key for the llm you would like to use for embeddings")
    elif normalized_command == "test":
        parser.add_argument("-b", "--baseline", dest="baseline_filename", required=True,
                            help="A file containing baseline data is required to run tests")
        parser.add_argument("-f", "--filename", dest="test_filename", required=True,
                            help="A file containing test data is required to run LLM tests")
        parser.add_argument("-o", "--output", dest="output_directory", required=True,
                            help="An output location is required for the test results")
        parser.add_argument("-llm", dest="query_llm", required=True,
                            help="An llm is required that you would like to generate a run queries against")
        parser.add_argument("-m", '--model', dest="query_model", required=True,
                            help="The model that for the llm that you would like to run queries against")
        parser.add_argument("-qkey", dest="query_api_key", required=True,
                            help="The api key for the llm you would like to use for querying")
        parser.add_argument("-ekey", dest="embeddings_api_key", required=True,
                            help="The api key for the llm you would like to use for embeddings, this must be the same llm and model as used in the baseline")
        parser.add_argument("-threshold", type=float, dest="success_threshold", required=True,
                            help="The threshold of similarity that determine the test passes")
    else:
        raise TypeError("Unknown command: " + command)

    return parser