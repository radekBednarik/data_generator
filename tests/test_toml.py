import pytest

from data_generator.toml import get_input


@pytest.fixture(scope="module", params=["data_config_example01.toml"])
def parsed_valid_toml(request):
    return get_input(request.param)


class TestToml:
    def test_get_input_from_valid_toml(self, parsed_valid_toml):
        assert isinstance(parsed_valid_toml, dict) is True
        assert parsed_valid_toml == dict(
            rows=50000,
            folder="output/test01",
            save_as="xlsx",
            specify=[
                dict(
                    data_type="int",
                    column_name="column1",
                    lower_bound=0,
                    upper_bound=1000,
                ),
                dict(
                    data_type="float",
                    column_name="column2",
                    lower_bound=-1000.0,
                    upper_bound=1000.0,
                ),
                dict(
                    data_type="str",
                    column_name="column3",
                    lower_bound=100,
                    upper_bound=100,
                ),
                dict(data_type="date", column_name="column4", format_template="%Y%m%d"),
                dict(data_type="timestamp", column_name="column5",),
            ],
        )
