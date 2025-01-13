import sys
import logging

from fruitstand.utils import argument_utils
from fruitstand.controllers import main

def start():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("http").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    
    command = sys.argv[1]

    parser = argument_utils.getArgumentParser(command)

    args, unknown = parser.parse_known_args()

    main.start(command, args)