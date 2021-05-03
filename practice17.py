a = list(map(int, input('ввести последовательность чисел через пробел: ').split()))
element = int(input(''))

def sort(b):
    for i in range(len(b)):
        for j in range(len(b) - i - 1):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]


def binary_search(array, element, left, right, prevMiddle):
    if left > right:  # если левая граница превысила правую,
        if element < prevMiddle:
            return left - 1  # значит элемент отсутствует
        else:
            return right

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle - 1  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1, array[middle])
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right, array[middle])

def search(a, element):
    return binary_search(a, element, 0, len(a), -1)

sorted_list = sort(a)
found = search(a, element)

if (found >= 0):
    print("Found: " + str(found))
else:
    print("not found")

