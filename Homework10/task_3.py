# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("test_input, expected", [pytest.param([1, 0], 0, marks=pytest.mark.xfail), ([1, 2], 0.5), ([1, 1, -2, 2], -0.25), ([5], 5), ([0, -1], 0), pytest.param([], 0, marks=pytest.mark.xfail)])
def test2_all_division(test_input, expected):
    assert all_division(*test_input) == expected
