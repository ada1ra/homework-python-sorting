from merge_sort import merge_sort, merge
from random import randint, uniform
import pytest

"""Тесты для функции merge"""

def test_merge_empty_lists():
    """Слияние двух пустых списков"""
    assert merge([], []) == []

def test_merge_left_empty():
    """Слияние когда левый список пустой"""
    assert merge([], [1, 2, 3]) == [1, 2, 3]

def test_merge_right_empty():
    """Слияние когда правый список пустой"""
    assert merge([1, 2, 3], []) == [1, 2, 3]

def test_merge_all_duplicates():
    """Слияние когда все элементы одинаковые"""
    left = [5, 5, 5]
    right = [5, 5]
    expected = [5, 5, 5, 5, 5]
    assert merge(left, right) == expected

def test_merge_single_element_lists():
    """Слияние списков из одного элемента"""
    assert merge([1], [2]) == [1, 2]
    assert merge([2], [1]) == [1, 2]

def test_merge_mixed_signs():
    """Слияние с числами разных знаков"""
    left = [-3, 0, 3]
    right = [-2, 1, 4]
    expected = [-3, -2, 0, 1, 3, 4]
    assert merge(left, right) == expected

def test_merge_float_numbers():
    """Слияние с числами с плавающей точкой"""
    left = [1.1, 2.2, 3.3]
    right = [1.5, 2.5, 3.5]
    expected = [1.1, 1.5, 2.2, 2.5, 3.3, 3.5]
    assert merge(left, right) == expected


"""Обычные тесты"""


@pytest.mark.parametrize(
    ["n"], [(([randint(0, 300) for _ in range(10)]),) for _ in range(10)]
)
def test_heap_sort_positive(n):
    """Тест с неотрицательными числами"""
    assert merge_sort(n) == sorted(n)


@pytest.mark.parametrize(
    ["n"], [(([randint(-300, -1) for _ in range(10)]),) for _ in range(10)]
)
def test_heap_sort_negative(n):
    """Тест с отрицательными числами"""
    assert merge_sort(n) == sorted(n)


@pytest.mark.parametrize(
    ["n"], [(([uniform(-50, 50) for _ in range(10)]),) for _ in range(10)]
)
def test_float_numbers(n):
    """Тест с числами с плавающей точкой"""
    assert merge_sort(n) == sorted(n)


"""Тесты крайних случаев"""


def test_empty_list():
    """Тест пустого списка"""
    assert merge_sort([]) == []


def test_single_element():
    """Тест одного элемента"""
    assert merge_sort([5]) == [5]

def test_odd_len():
    """Тест массива с нечётным количеством элементов"""
    assert merge_sort([5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]

def test_large_random_list():
    """Тест большого случайного списка"""
    test_list = [randint(-1000, 1000) for _ in range(1000)]
    assert merge_sort(test_list) == sorted(test_list)


def test_very_large_numbers():
    """Тест с очень большими числами"""
    assert merge_sort([2 ** 100, 0, -1, -2 ** 11]) == [-2 ** 11, -1, 0, 2 ** 100]


def test_already_sorted():
    """Тест уже отсортированного массива"""
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_duplicates():
    """Тест с дубликатами"""
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]
