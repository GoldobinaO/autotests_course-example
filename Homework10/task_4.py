# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import time
import pytest
from task_2 import all_division


class TestClass:
    @pytest.fixture()
    def fixture_time(self):
        start = time.time()
        yield
        end = time.time()
        print(' duration:', end - start)

    def test1_all_division(self):
        with pytest.raises(ZeroDivisionError):
            all_division(1, 0)

    def test2_all_division(self, fixture_time):
        assert all_division(1, 2) == 0.5

    def test3_all_division(self, fixture_time):
        assert all_division(1, 1, -2, 2) == -0.25

    def test4_all_division(self):
        assert all_division(5) == 5

    def test5_all_division(self):
        assert all_division(0, -1) == 0

    def test6_all_division(self, fixture_time):
        with pytest.raises(IndexError):
            all_division()
