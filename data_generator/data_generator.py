# DEBUG
from pprint import PrettyPrinter
from typing import Any, Optional, Dict

from cli_parser import parse_inputs, verify, convert_args

printer: Any = PrettyPrinter(indent=2, sort_dicts=False)

if __name__ == "__main__":
    args: Any = parse_inputs()
    args_dict: Dict[str, str] = vars(args)
    print(args_dict)
    print(args.specify)
    print(args.rows)
    print(args.folder)

    result: Optional[int] = verify(args)
    print(result)

    printer.pprint(convert_args(vars(args)))
