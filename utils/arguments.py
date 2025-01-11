from argparse import ArgumentParser

def getArgumentParser(command):
    parser = ArgumentParser()

    if command.lower() == "baseline":
        parser.add_argument("-f", "--filename", dest="filename",
                            help="A file containing test data is required to generate an LLM baseline")
        parser.add_argument("-o", "--output", dest="output",
                            help="An output location is required for the baseline data")
        parser.add_argument("-llm", dest="llm",
                            help="An llm is required that you would like to generate a baseline for")
        parser.add_argument("-m", '--model', dest="model",
                            help="The model that for the llm that you would like to generate a baseline for")

        return parser