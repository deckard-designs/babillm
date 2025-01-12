import sys

from fruitstand.utils import argument_utils
from fruitstand.controllers import main

def start():
    command = sys.argv[1]

    parser = argument_utils.getArgumentParser(command)

    args, unknown = parser.parse_known_args()

    main.start(command, args)