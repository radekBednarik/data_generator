import sys

import pytest

from data_generator.cli_parser import parse_inputs, verify


@pytest.fixture(
    scope="module",
    params=[
        [
            # "python3",
            # "-m",
            "data_generator",
            "-sa",
            "xlsx",
            "-f",
            "output/test",
            "data",
            "column1:str:0:50",
            "column2:str:101:101",
            "column3:int:10:10",
            "column4:int:0:1000",
            "column5:float:0.0:1000.0",
            "1000",
        ],
        [
            # "python3",
            # "-m",
            "data_generator",
            "toml",
            "data_config_example01.toml",
            "data_config_example02.toml",
        ],
    ],
)
def valid_cli_input(request):
    return request.param


class TestFuncParseInputs:
    def test_with_valid_inputs(self, valid_cli_input):
        sys.argv = valid_cli_input
        parsed_inputs = parse_inputs()

        # data_parser
        if hasattr(parsed_inputs, "specify"):
            assert vars(parsed_inputs) == dict(
                folder="output/test",
                save_as="xlsx",
                specify=[
                    "column1:str:0:50",
                    "column2:str:101:101",
                    "column3:int:10:10",
                    "column4:int:0:1000",
                    "column5:float:0.0:1000.0",
                ],
                rows=1000,
            )

        # TOML parser
        if hasattr(parsed_inputs, "toml"):
            assert vars(parsed_inputs) == dict(
                # defaults in CLI parser!!!
                folder="output",
                save_as="csv",
                toml=["data_config_example01.toml", "data_config_example02.toml",],
            )


class TestFuncVerify:
    def test_with_correctly_parsed_inputs(self, valid_cli_input):
        sys.argv = valid_cli_input
        parsed_inputs = parse_inputs()

        assert verify(parsed_inputs) is None
