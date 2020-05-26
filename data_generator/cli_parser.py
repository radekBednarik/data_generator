import argparse
import re
from typing import Optional, Union


def parse_inputs() -> argparse.Namespace:
    """Processes CLI input and returns argparse Namespace with entered arguments' values.

    Returns:
        Any -- argparse.Namespace subclass.

    See:
        https://docs.python.org/3/library/argparse.html#argparse.Namespace
    """
    # create parsers
    main_parser = argparse.ArgumentParser(
        description="Use -h or --help to display available commands."
    )
    subparsers = main_parser.add_subparsers(
        help="Use some of these commands with -h or --help do display help."
    )
    data_parser = subparsers.add_parser(
        "data", help="Specify data you want to have generated."
    )
    toml_parser = subparsers.add_parser(
        "toml",
        help="Enter filepath(s) to .toml files with data configuration(s) you want to have generated.",
    )
    # DATA parser args
    data_parser.add_argument(
        "specify",
        action="extend",
        nargs="+",
        type=str,
        help="Specify columns, their datatype and max size.\nExamples: \
            String: column1:str:0:50\n \
            Float:  column2:float:-100:100\n \
            Int: column3:int:-100:100\n \
            Date: column4:date:%Y%m%d_%H%M%S",
    )
    data_parser.add_argument(
        "rows",
        action="store",
        type=int,
        help="Specify number of rows to be generated, header is excluded.",
    )
    # TOML parser args
    toml_parser.add_argument(
        "toml",
        action="extend",
        nargs="+",
        type=str,
        help="Specify filepath(s) to .toml files with data specifications.",
    )
    # MAIN parser args
    main_parser.add_argument(
        "-f",
        "--folder",
        action="store",
        type=str,
        default="output",
        help="Folder, where generated data are stored. If not provided, defaults to './output'",
    )
    main_parser.add_argument(
        "-sa",
        "--save_as",
        action="store",
        type=str,
        default="csv",
        help="Specify file format of the output. Options are 'csv', 'json'. If not provided, defaults to 'csv'.",
    )
    return main_parser.parse_args()


def verify(inputs: argparse.Namespace) -> Optional[int]:
    """Verifies parsed CLI input strings.

    Arguments:
        inputs -- parsed CLI input via func parse_inputs()

    Raises:
        RuntimeError: if some argument does not pass verification, this exception is raised

    Returns:
        None: OK, 1: NOK, if RuntimeError is raised and caught
    """
    regex = re.compile(
        r"(^[a-zA-Z0-9_]+:str:\d+:\d+$)|(^[a-zA-Z0-9_]+:(int):-?\d+:\d+$)|(^[a - zA - Z0 - 9_] + : (float): - ?\d+\.\d*:\d+\.\d*$)|(^[A-Za-z0-9_]+:date:[A-Za-z%_\-]*$)|(^[A-Za-z0-9_]+:timestamp:$)"
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


def convert_args(args: argparse.Namespace) -> dict:
    """Does conversion of parsed CLI args, which are all {str} into suitable 
    format and datatypes.

    Arguments:
        args -- parsed CLI arguments as argparse.Namespace

    Returns:
        converted cli arguments as dictionary
    """

    def assign(chunks: list) -> Union[int, dict]:
        """Transforms and assigns values of data args. Returns dict.

        Arguments:
            chunks -- list of chunks of string splitted by given parameter

        Returns:
            dict with assigned values and converted values, 1: Nothing was returned
        """
        if chunks[1] in ("str", "int", "float"):
            return dict(
                data_type=chunks[1],
                column_name=chunks[0],
                lower_bound=float(chunks[2]),
                upper_bound=float(chunks[3]),
            )
        if chunks[1] in ("date"):
            return dict(
                data_type=chunks[1], column_name=chunks[0], format_template=chunks[2]
            )
        if chunks[1] in ("timestamp"):
            return dict(data_type=chunks[1], column_name=chunks[0])
        return 1

    output = {}
    args_ = vars(args)

    for key, value in iter(args_.items()):
        if key not in list(output.keys()):
            output[key] = None

        if key == "specify":
            output[key] = []
            for v in value:
                chunks = v.split(sep=":")

                if chunks[1] == "str":
                    output[key].append(assign(chunks))
                elif chunks[1] == "int":
                    output[key].append(assign(chunks))
                elif chunks[1] == "float":
                    output[key].append(assign(chunks))
                elif chunks[1] == "date":
                    output[key].append(assign(chunks))
                elif chunks[1] == "timestamp":
                    output[key].append(assign(chunks))

        elif key == "toml":
            output[key] = []
            for item in value:
                output[key].append(item)

        elif key == "rows":
            output[key] = int(value)

        elif key == "folder":
            output[key] = value

        elif key == "save_as":
            output[key] = value

    return output
