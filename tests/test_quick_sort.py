from quick_sort import quick_sort
from random import randint, uniform
import pytest

"""Обычные тесты"""

@pytest.mark.parametrize(
    ["n"], [(([randint(0, 300) for _ in range(10)]),) for _ in range(10)]
)
def test_heap_sort_positive(n):
    """Тест с неотрицательными числами"""
    assert quick_sort(n) == sorted(n)


@pytest.mark.parametrize(
    ["n"], [(([randint(-300, -1) for _ in range(10)]),) for _ in range(10)]
)
def test_heap_sort_negative(n):
    """Тест с отрицательными числами"""
    assert quick_sort(n) == sorted(n)


@pytest.mark.parametrize(
    ["n"], [(([uniform(-50, 50) for _ in range(10)]),) for _ in range(10)]
)
def test_float_numbers(n):
    """Тест с числами с плавающей точкой"""
    assert quick_sort(n) == sorted(n)


"""Тесты крайних случаев"""


def test_empty_list():
    """Тест пустого списка"""
    assert quick_sort([]) == []


def test_single_element():
    """Тест одного элемента"""
    assert quick_sort([5]) == [5]


def test_large_random_list():
    """Тест большого случайного списка"""
    test_list = [randint(-1000, 1000) for _ in range(1000)]
    assert quick_sort(test_list) == sorted(test_list)


def test_very_large_numbers():
    """Тест с очень большими числами"""
    assert quick_sort([2 ** 100, 0, -1, -2 ** 11]) == [-2 ** 11, -1, 0, 2 ** 100]


def test_already_sorted():
    """Тест уже отсортированного массива"""
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_duplicates():
    """Тест с дубликатами"""
    assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]
