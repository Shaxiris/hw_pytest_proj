def get(arr, i, default=None):
    """
    Извлекает из списка значение по указанному индексу, если индекс существует.
    Если индекс не существует, возвращает значение по умолчанию.
    """
    if i < 0 or i >= len(arr):
        return default
    else:
        return arr[i]

def my_slice(arr, start, end=None):
    """
    Возвращает срез заданного массива, аналогично встроенной функции среза..
    """
    if end is None:
        end = len(arr)
    return arr[start:end]

def swap(arr, i, j):
    """
    Меняет местами элементы по заданным индексам в заданном массиве.
    """
    arr[i], arr[j] = arr[j], arr[i]

def remove_duplicates(arr):
    """
    Удаляет дубликаты из заданного массива, сохраняя порядок элементов.
    """
    seen = set()
    result = []
    for elem in arr:
        if elem not in seen:
            seen.add(elem)
            result.append(elem)
    return result

def concatenate(arr1, arr2):
    """
    Возвращает конкатенацию заданных массивов.
    """
    return arr1 + arr2
