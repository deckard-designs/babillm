from fruitstand.controllers import baseline, test

def start(command, args):
    normalized_command = command.lower()


    if normalized_command == "baseline":
        baseline.start(args)
    elif normalized_command == "test":
        test.start(args)
    else:
        raise TypeError("Unknown command: " + command)