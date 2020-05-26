import argparse
from typing import List, Union

# pyre-ignore
from data_generator.cli_parser import convert_args, parse_inputs, verify
from data_generator.generator import assemble_data_generators
from data_generator.output import to_csv, to_excel, to_json
from data_generator.toml import get_input


def run_cli_inputs(args: argparse.Namespace) -> Union[tuple, int]:
    """Returns data generators and other needed args, when user uses CLI to enter inputs.

    Arguments:
        args {argparse.Namespace} -- args entered via CLI

    Returns:
        Union[tuple, int] -- (data generators dict, cli args dict), 1: if NOK
    """
    if verify(args) is None:
        converted_args = convert_args(args)

        print("--> Parsed CLI inputs converted to dictionary.\r\n")

        result = assemble_data_generators(converted_args)

        print("--> Data generators created.\r\n")

        return (result, converted_args)
    return 1


def run_toml_inputs(args: argparse.Namespace) -> Union[List[int], List[tuple]]:
    """Retruns data generators and other needed args, when user uses TOML files to provide inputs.

    Arguments:
        args {argparse.Namespace} -- args entered via CLI

    Returns:
        Union[List[tuple], List[int]] -- list of (data generators dict, cli args dict), 1: if NOK
    """
    output = []

    try:
        converted_args = convert_args(args)

        print("--> Parsed CLI inputs converted to dictionary.\r\n")

        if len(converted_args["toml"]) > 0:
            for filepath in converted_args["toml"]:
                conf_dict = get_input(filepath)
                result = assemble_data_generators(conf_dict)

                print("--> Data generators created.\r\n")

                output.append((result, conf_dict))
            return output
        return [1]
    except Exception as e:
        print(f"Exception in func 'run_toml_inputs': {str(e)}")
        return [1]


def run_outputs(inputs: Union[tuple, int]) -> None:
    """Generates data via generators and saves them to specified file format.

    Arguments:
        inputs {tuple} -- (data generators dict, cli args dict)
    """
    print("--> Data generation and saving starting... \n")

    if inputs[1]["save_as"] == "json":
        to_json(inputs[0], inputs[1]["rows"], inputs[1]["folder"])
    elif inputs[1]["save_as"] == "xlsx":
        to_excel(inputs[0], inputs[1]["rows"], inputs[1]["folder"])
    else:
        to_csv(inputs[0], inputs[1]["rows"], inputs[1]["folder"])

    print(f"""\n--> FINISHED. Find your data at '{inputs[1]["folder"]}' folder.""")


def main() -> None:
    args = parse_inputs()

    print("--> CLI input parsed\r\n")

    if hasattr(args, "specify"):
        output = run_cli_inputs(args)
        run_outputs(output)

    if hasattr(args, "toml"):
        outputs = run_toml_inputs(args)
        for output in outputs:
            run_outputs(output)


if __name__ == "__main__":
    main()
