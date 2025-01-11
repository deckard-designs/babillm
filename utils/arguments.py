from argparse import ArgumentParser

def getArgumentParser(command):
    parser = ArgumentParser()

    if command.lower() == "baseline":
        parser.add_argument("-f", "--filename", dest="filename",
                            help="A file containing test data is required to generate an LLM baseline")
        parser.add_argument("-o", "--output", dest="output",
                            help="An output location is required for the baseline data")
        parser.add_argument("-qllm", dest="query_llm",
                            help="An llm is required that you would like to generate a baseline queries for")
        parser.add_argument("-qm", '--model', dest="query_model",
                            help="The model that for the llm that you would like to generate a baseline queries for")
        parser.add_argument("-qkey", '--model', dest="query_api_key",
                            help="The api key for the llm you would like to use for querying")
        parser.add_argument("-ellm", dest="embeddings_llm",
                            help="An llm is required that you would like to use to generate embeddings")
        parser.add_argument("-em", dest="embeddings_model",
                            help="An model is required that you would like to use to generate embeddings")
        parser.add_argument("-ekey", '--model', dest="embeddings_api_key",
                            help="The api key for the llm you would like to use for embeddings")

        return parser