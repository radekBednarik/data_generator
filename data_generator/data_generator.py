# DEBUG
from typing import Any

from cli_parser import parse_inputs

if __name__ == "__main__":
    args: Any = parse_inputs()

    print(vars(args))
    print(args.specify)
    print(args.folder)
