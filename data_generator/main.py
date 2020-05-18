# DEBUG
from pprint import PrettyPrinter
from typing import Any, Optional, Dict

from cli_parser import parse_inputs, verify, convert_args
from generator import generate_string, generate_int

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

    specs = convert_args(vars(args))
    printer.pprint(convert_args(vars(args)))
    r_str: str = generate_string(
        specs["specify"][0]["lower_bound"], specs["specify"][0]["upper_bound"]
    )
    print(r_str)
    r_int: int = generate_int(
        specs["specify"][2]["lower_bound"], specs["specify"][2]["upper_bound"]
    )
    print(r_int)
