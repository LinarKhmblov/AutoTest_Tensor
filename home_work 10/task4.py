# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.my_fixture
class TestAllDivision():

    @pytest.mark.my_fixture
    def test_division_by_zero(self, test_fixture):
        with pytest.raises(ZeroDivisionError):
            assert all_division(1, 0)

    def test_division_two_numbers(self):
        assert all_division(4, 2) == 2

    @pytest.mark.my_fixture
    def test_division_three_numbers(self, test_fixture):
        assert all_division(16, 4, 2) == 2
