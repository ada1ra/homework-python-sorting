def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Базовый случай: массив из 0 или 1 элемента уже отсортирован

    pivot = arr[len(arr) // 2]  # Выбираем середину в качестве опорного элемента

    left = [x for x in arr if x < pivot]  # Массив элементов меньше опорного
    middle = [x for x in arr if x == pivot]  # Массив элементов, равных опорному
    right = [x for x in arr if x > pivot]  # Массив элементов больше опорного

    # Рекурсивно сортируем левую и правую части, объединяем все вместе
    return quick_sort(left) + middle + quick_sort(right)
