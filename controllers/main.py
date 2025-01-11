from controllers import baseline

def start(command, args):
    if command.lower() == "baseline":
        baseline.start(args)
    else:
        raise TypeError("Unknown command: " + command)