# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами, скрины с вызовами и их результаты.

import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

# Тест деление двух чисел
@pytest.mark.smoke
def test_division_two_numbers():
    assert all_division(25, 5) == 5

# Тест деление четырех чисел
@pytest.mark.smoke
def test_division_four_numbers():
    assert all_division(99, 3, 11, 3) == 1

#  Тест деление на ноль
@pytest.mark.by_zero
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert all_division(1, 0)

# Тест с аргументами, включающими строковое значение
@pytest.mark.negative
def test_division_by_string():
    with pytest.raises(TypeError):
        assert all_division(10, '5')

# Тест с аргументами, включающими строковое значение
@pytest.mark.negative
def test_division_by_not_int():
    with pytest.raises(TypeError):
        assert all_division(5, [3, 4])


