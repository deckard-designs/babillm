import sys

from utils import argument_utils
from controllers import main

command = sys.argv[1]

parser = argument_utils.getArgumentParser(command)

args, unknown = parser.parse_known_args()

main.start(command, args)