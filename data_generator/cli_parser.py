import argparse
from typing import Any


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
            String: column1:str:50\n \
            Float:  column2:float:-100:100\n \
            Int:    column3:int:-100:100",
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
