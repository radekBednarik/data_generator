# DEBUG
from typing import Any, Optional

from cli_parser import parse_inputs, verify

if __name__ == "__main__":
    args: Any = parse_inputs()

    print(vars(args))
    print(args.specify)
    print(args.folder)

    result: Optional[int] = verify(args)
    print(result)
