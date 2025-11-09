def merge(left, right):
    """
    Сливает два отсортированных массива в один отсортированный
    
    Args:
        left: левый отсортированный массив
        right: правый отсортированный массив
    
    Returns:
        объединенный отсортированный массив
    """
    result = []
    i = j = 0  # указатели для left и right
    
    # Сравниваем элементы и добавляем меньший в результат
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Добавляем оставшиеся элементы (если есть)
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort(arr):
    """
    Основная функция сортировки слиянием
    
    Args:
        arr: массив для сортировки
    
    Returns:
        отсортированный массив
    """
    # Базовый случай: массивы длиной 0 или 1 уже отсортированы
    if len(arr) <= 1:
        return arr
    
    # Разделяем массив на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Рекурсивно сортируем каждую половину
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Сливаем отсортированные половины
    return merge(left_sorted, right_sorted)
