from heap_sort import heap_sort, heapify
from random import randint, uniform
import pytest

"""Тесты для функции heapify"""

def is_max_heap(arr, n):
    """Дополнительная функция, проверяет что массив удовлетворяет свойству max-heap"""
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True

def test_heapify_empty():
    """Тест пустого массива"""
    arr = []
    heapify(arr, 0, 0)
    assert arr == []

def test_heapify_single_element():
    """Тест массива из одного элемента"""
    arr = [5]
    heapify(arr, 1, 0)
    assert arr == [5]

def test_heapify_with_duplicates():
    """Тест с дубликатами"""
    arr = [5, 5, 5, 3, 5, 2]
    n = len(arr)
    heapify(arr, n, 0)
    assert is_max_heap(arr, n)

def test_heapify_negative_numbers():
    """Тест с отрицательными числами"""
    arr = [-1, -3, -2, -7, -5]
    n = len(arr)
    heapify(arr, n, 0)
    assert is_max_heap(arr, n)

def test_heapify_large_numbers():
    """Тест с большими числами"""
    arr = [1000, 500, 1500, 200, 300]
    n = len(arr)
    heapify(arr, n, 0)
    assert is_max_heap(arr, n)

def test_heapify_only_left_child():
    """Тест, когда есть только левый потомок"""
    arr = [1, 3, 2]  # У узла 0 есть только левый потомок 3
    n = len(arr)
    heapify(arr, n, 0)
    assert arr == [3, 1, 2]  # 3 становится корнем

def test_heapify_already_max():
    """Тест, когда корень уже максимальный"""
    arr = [10, 5, 8, 3, 4, 6, 7]
    n = len(arr)
    original = arr.copy()
    heapify(arr, n, 0)
    # Ничего не должно измениться
    assert arr == original


"""Обычные тесты"""


@pytest.mark.parametrize(
    ["n"], [(([randint(0, 300) for _ in range(10)]),) for _ in range(10)]
)
def test_heap_sort_positive(n):
    """Тест с неотрицательными числами"""
    assert heap_sort(n) == sorted(n)


@pytest.mark.parametrize(
    ["n"], [(([randint(-300, -1) for _ in range(10)]),) for _ in range(10)]
)
def test_heap_sort_negative(n):
    """Тест с отрицательными числами"""
    assert heap_sort(n) == sorted(n)


@pytest.mark.parametrize(
    ["n"], [(([uniform(-50, 50) for _ in range(10)]),) for _ in range(10)]
)
def test_float_numbers(n):
    """Тест с числами с плавающей точкой"""
    assert heap_sort(n) == sorted(n)


"""Тесты крайних случаев"""


def test_empty_list():
    """Тест пустого списка"""
    assert heap_sort([]) == []


def test_single_element():
    """Тест одного элемента"""
    assert heap_sort([5]) == [5]


def test_large_random_list():
    """Тест большого случайного списка"""
    test_list = [randint(-1000, 1000) for _ in range(1000)]
    assert heap_sort(test_list) == sorted(test_list)


def test_very_large_numbers():
    """Тест с очень большими числами"""
    assert heap_sort([2 ** 100, 0, -1, -2 ** 11]) == [-2 ** 11, -1, 0, 2 ** 100]


def test_already_sorted():
    """Тест уже отсортированного массива"""
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_duplicates():
    """Тест с дубликатами"""
    assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]
