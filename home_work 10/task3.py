# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('numbers', [
    (10, 5),
    (100, 10, 5),
    pytest.param((100, 10, 2, 2), marks=pytest.mark.skip),
    (1000, 10, 5, 2, 2)
])
@pytest.mark.parametrize('smoke', [True, False], ids=['smoke', 'not smoke'])
def test_division(numbers, smoke):
    if smoke:
        pytest.skip('Пропускаем smoke тест.')
    expected_result = numbers[0] / numbers[1]
    for i in numbers[2:]:
        expected_result /= i
    assert all_division(*numbers) == expected_result

