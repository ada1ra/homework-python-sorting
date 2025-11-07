from bubble_sort import bubble_sort
from random import randint, uniform
import pytest

"""Обычные тесты"""


@pytest.mark.parametrize(
    ["n"], [(([randint(0, 300) for _ in range(10)]),) for _ in range(10)]
)
def test_heap_sort_positive(n):
    """Тест с неотрицательными числами"""
    assert bubble_sort(n) == sorted(n)


@pytest.mark.parametrize(
    ["n"], [(([randint(-300, -1) for _ in range(10)]),) for _ in range(10)]
)
def test_heap_sort_negative(n):
    """Тест с отрицательными числами"""
    assert bubble_sort(n) == sorted(n)


@pytest.mark.parametrize(
    ["n"], [(([uniform(-50, 50) for _ in range(10)]),) for _ in range(10)]
)
def test_float_numbers(n):
    """Тест с числами с плавающей точкой"""
    assert bubble_sort(n) == sorted(n)


"""Тесты крайних случаев"""


def test_empty_list():
    """Тест пустого списка"""
    assert bubble_sort([]) == []


def test_single_element():
    """Тест одного элемента"""
    assert bubble_sort([5]) == [5]


def test_large_random_list():
    """Тест большого случайного списка"""
    test_list = [randint(-1000, 1000) for _ in range(1000)]
    assert bubble_sort(test_list) == sorted(test_list)


def test_very_large_numbers():
    """Тест с очень большими числами"""
    assert bubble_sort([2 ** 100, 0, -1, -2 ** 11]) == [-2 ** 11, -1, 0, 2 ** 100]


def test_already_sorted():
    """Тест уже отсортированного массива"""
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Тест обратно сортированного массива"""
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_duplicates():
    """Тест с дубликатами"""
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]
