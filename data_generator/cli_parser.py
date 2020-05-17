import argparse
import re
from typing import Any, Dict, Optional, List, Union, Type


def parse_inputs() -> Any:
    """Processes CLI input and returns argparse Namespace with entered arguments' values.

    Returns:
        Any -- argparse.Namespace subclass.

    See:
        https://docs.python.org/3/library/argparse.html#argparse.Namespace
    """
    # create parsers
    main_parser: Any = argparse.ArgumentParser(
        description="Use -h or --help to display available commands."
    )
    subparsers: Any = main_parser.add_subparsers(
        help="Use some of these commands with -h or --help do display help."
    )
    data_parser: Any = subparsers.add_parser(
        "data", help="Specify data you want to have generated."
    )
    # DATA
    data_parser.add_argument(
        "specify",
        action="extend",
        nargs="+",
        type=str,
        help="Specify columns, their datatype and max size.\nExamples: \
            String: column1:str:0:50\n \
            Float:  column2:float:-100:100\n \
            Int:    column3:int:-100:100",
    )
    data_parser.add_argument(
        "rows",
        action="store",
        type=int,
        help="Specify number of rows to be generated, header is excluded.",
    )
    data_parser.add_argument(
        "-f",
        "--folder",
        action="store",
        type=str,
        default="output",
        help="Folder, where generated data are stored. If not provided, defaults to './output'",
    )
    return main_parser.parse_args()


def verify(inputs: Any) -> Optional[int]:
    """Verifies parsed CLI input strings.

    Arguments:
        inputs {Any} -- parsed CLI input via func parse_inputs()

    Raises:
        RuntimeError: if some argument does not pass verification, this exception is raised

    Returns:
        Optional[int] -- None: OK, 1: NOK, if RuntimeError is raised and caught
    """
    regex: Any = re.compile(
        r"(^[a-zA-Z0-9_]+:str:\d+:\d+$)|(^[a-zA-Z0-9_]+:(int|float):-?\d+:\d+$)"
    )

    try:
        if inputs.specify is not None:
            for input_ in inputs.specify:
                if regex.search(input_) is None:
                    raise RuntimeError(
                        f"Provided argument '{input_}' has wrong format.\r\nPlease check documentation and try again."
                    )

        if inputs.rows <= 0:
            raise RuntimeError(
                f"You can not generate '{str(inputs.rows)}' rows. Minimum number is 1."
            )
    except RuntimeError as e:
        print(str(e))
        return 1

    return None


def convert_args(args: Dict[str, str]) -> Any:
    output: dict = {}

    for key, value in iter(args.items()):
        # if key not in output dict, add it
        if key not in list(output.keys()):
            output[key] = []

        if key == "specify":
            for v in value:
                chunks: List[str] = v.split(sep=":")
                temp_dict: Dict[
                    str, Union[Type[str], Type[int], Type[float], int, str]
                ] = {}

                if chunks[1] == "str":
                    temp_dict = dict(
                        data_type=str,
                        column_name=chunks[0],
                        lower_bound=int(chunks[2]),
                        upper_bound=int(chunks[3]),
                    )
                    output[key].append(temp_dict)

                elif chunks[1] == "int":
                    temp_dict = dict(
                        data_type=int,
                        column_name=chunks[0],
                        lower_bound=int(chunks[2]),
                        upper_bound=int(chunks[3]),
                    )
                    output[key].append(temp_dict)

                elif chunks[1] == "float":
                    temp_dict = dict(
                        data_type=float,
                        column_name=chunks[0],
                        lower_bound=int(chunks[2]),
                        upper_bound=int(chunks[3]),
                    )
                    output[key].append(temp_dict)

    return output
