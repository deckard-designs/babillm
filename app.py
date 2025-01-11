import sys

from utils import arguments
from controllers import main

command = sys.argv[1]

parser = arguments.getArgumentParser(command)

args, unknown = parser.parse_known_args()

main.start(command, args)