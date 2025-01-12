from argparse import ArgumentParser

def getArgumentParser(command):
    parser = ArgumentParser()

    normalized_command = command.lower()

    if normalized_command == "baseline":
        parser.add_argument("-f", "--filename", dest="filename",
                            help="A file containing test data is required to generate an LLM baseline")
        parser.add_argument("-o", "--output", dest="output_directory",
                            help="An output location is required for the baseline data")
        parser.add_argument("-qllm", dest="query_llm",
                            help="An llm is required that you would like to generate a baseline queries for")
        parser.add_argument("-qm", '--model', dest="query_model",
                            help="The model that for the llm that you would like to generate a baseline queries for")
        parser.add_argument("-qkey", dest="query_api_key",
                            help="The api key for the llm you would like to use for querying")
        parser.add_argument("-ellm", dest="embeddings_llm",
                            help="An llm is required that you would like to use to generate embeddings")
        parser.add_argument("-em", dest="embeddings_model",
                            help="An model is required that you would like to use to generate embeddings")
        parser.add_argument("-ekey", dest="embeddings_api_key",
                            help="The api key for the llm you would like to use for embeddings")
    elif normalized_command == "test":
        parser.add_argument("-b", "--baseline", dest="baseline_filename",
                            help="A file containing baseline data is required to run tests")
        parser.add_argument("-f", "--filename", dest="test_filename",
                            help="A file containing test data is required to run LLM tests")
        parser.add_argument("-o", "--output", dest="output_directory",
                            help="An output location is required for the test results")
        parser.add_argument("-llm", dest="query_llm",
                            help="An llm is required that you would like to generate a run queries against")
        parser.add_argument("-m", '--model', dest="query_model",
                            help="The model that for the llm that you would like to run queries against")
        parser.add_argument("-qkey", dest="query_api_key",
                            help="The api key for the llm you would like to use for querying")
        parser.add_argument("-ekey", dest="embeddings_api_key",
                            help="The api key for the llm you would like to use for embeddings, this must be the same llm and model as used in the baseline")
    else:
        raise TypeError("Unknown command: " + command)

    return parser