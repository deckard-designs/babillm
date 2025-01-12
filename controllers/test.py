import json

from schemas import test_data_schema

def start(args):
    with open(args.baseline_filename, 'r') as file:
        baseline_data = json.load(file)

    with open(args.test_filename, 'r') as file:
        test_data = json.load(file)

    
    test_data_schema.validate(test_data)

    