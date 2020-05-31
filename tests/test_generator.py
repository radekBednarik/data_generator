import inspect

import pytest

from data_generator.generator import (
    _generator,
    random_date,
    random_float,
    random_int,
    random_string,
    random_timestamp,
)


@pytest.fixture(
    scope="module",
    params=[
        [random_date, None, None, "%Y%m%d"],
        [random_float, 1000.0, 0.0, None],
        [random_int, 100, 90, None],
        [random_string, 10, 10, None],
        [random_timestamp, None, None, None],
    ],
    ids=[
        "random date params",
        "random float params",
        "random int params",
        "random string params",
        "random timestamp params",
    ],
)
def params_for_generator(request):
    return request.param


class Test_Generator:
    def test_generator_created(self, params_for_generator):
        generator_ = _generator(
            params_for_generator[0],
            upper_bound=params_for_generator[1],
            lower_bound=params_for_generator[2],
            date_template=params_for_generator[3],
        )
        assert inspect.isgenerator(generator_) is True
