from subprocess import run


class TestFunctional:
    def test_input_method_cli(self):
        result = run(
            "python3 -m data_generator -sa csv -f output/test01 data integers:int:900:1000 float:float:-1000.0:1000.0 strings:str:60:60 date:date:%Y%m%d timestamp:timestamp: 100000",
            capture_output=True,
            check=True,
            shell=True,
            text=True,
        )
        assert result.returncode == 0
        assert "Could not generate data and save them" not in result.stdout

    def test_input_method_toml(self):
        result = run(
            "python3 -m data_generator toml data_config_example01.toml data_config_example02.toml",
            capture_output=True,
            check=True,
            shell=True,
            text=True,
        )
        assert result.returncode == 0
        assert "Could not generate data and save them" not in result.stdout
