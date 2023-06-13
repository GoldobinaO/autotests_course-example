# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


def test1_all_division():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 0)


def test2_all_division():
    assert all_division(1, 2) == 0.5


def test3_all_division():
    assert all_division(1, 1, -2, 2) == -0.25


def test4_all_division():
    assert all_division(5) == 5


def test5_all_division():
    assert all_division(0, -1) == 0


def test6_all_division():
    with pytest.raises(IndexError):
        all_division()
