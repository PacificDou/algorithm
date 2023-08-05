
def binarySearch_v2(array, key):
    left = 0
    right = len(array) - 1
    idx = -1
    while left + 1 < right:
        mid = (left + right) // 2
        if array[mid] == key:
            idx = mid
            break
        if array[mid] < key:
            left = mid
        elif array[mid] > key:
            right = mid

    if idx < 0:
        if array[left] == key:
            idx = left
        elif array[right] == key:
            idx = right

    return idx


# if there are multiple elements same as search key, return the first index
def binarySearchFirst_v2(array, key):
    left = 0
    right = len(array) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if array[mid] == key:
            right = mid
        if array[mid] < key:
            left = mid
        elif array[mid] > key:
            right = mid

    idx = -1
    if array[left] == key:
        idx = left
    elif array[right] == key:
        idx = right

    return idx


# if there are multiple elements same as search key, return the last index
def binarySearchLast_v2(array, key):
    left = 0
    right = len(array) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if array[mid] == key:
            left = mid
        if array[mid] < key:
            left = mid
        elif array[mid] > key:
            right = mid

    idx = -1
    if array[right] == key:
        idx = right
    elif array[left] == key:
        idx = left

    return idx


def test(array, key):
    print('----------------------------------------')
    print(array, key)
    print('binarySearch_v2:        {}'.format(binarySearch_v2(array, key)))
    print('binarySearchFirst_v2:   {}'.format(binarySearchFirst_v2(array, key)))
    print('binarySearchLast_v2:    {}'.format(binarySearchLast_v2(array, key)))


if __name__ == '__main__':
    array = [-1, 1, 3, 3, 7, 7, 7, 7, 9, 9]
    for key in range(-2, 11):
        test(array, key)
