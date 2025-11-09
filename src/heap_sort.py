# преобразование в двоичную кучу с корнем i (индекс в arr); n - размер кучи
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # проверяем существует ли левый дочерний элемент больший, чем корень
    if left < n and arr[i] < arr[left]:
        largest = left

    # проверяем существует ли правый дочерний элемент больший, чем корень
    if right < n and arr[largest] < arr[right]:
        largest = right

    # заменяем корень, если нашёлся элемент больше
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # применяем heapify к корню
        heapify(arr, n, largest)


# сортировка массива (основная функция)
def heap_sort(arr):
    n = len(arr)

    # строим max-heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # переворачиваем массив
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # свап
        heapify(arr, i, 0)

    return arr
