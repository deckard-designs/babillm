import json

from schemas import baseline_schema
from factories import llm_factory

def start(args):
    with open(args.filename, 'r') as file:
        data = json.load(file)
        
    baseline_schema.validate(data)

    llService = llm_factory.getLLM(args.llm)

    supported_model = llService.validateModel(args.model)

    if (supported_model == False):
        raise TypeError(f"{args.model} is not a valid model for {args.llm}")