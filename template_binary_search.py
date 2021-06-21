# https://www.topcoder.com/thrive/articles/Binary%20Search


def binarySearch(array, key):
    left = 0
    right = len(array) - 1
    idx = -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            idx = mid
            break
        if array[mid] < key:
            left = mid + 1
        elif array[mid] > key:
            right = mid - 1

    return idx


# if there are multiple elements same as search key, return the first index
def binarySearchFirst(array, key):
    left = 0
    right = len(array) - 1
    idx = -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            idx = mid
            right = mid - 1
            # these two lines can also be removed, but will be less efficient
            if not (left <= right and array[right] == key):
                break
        elif array[mid] < key:
            left = mid + 1
        elif array[mid] > key:
            right = mid - 1

    return idx


# if there are multiple elements same as search key, return the last index
def binarySearchLast(array, key):
    left = 0
    right = len(array) - 1
    idx = -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            idx = mid
            left = mid + 1
            # these two lines can also be removed, but will be less efficient
            if not (left <= right and array[left] == key):
                break
        elif array[mid] < key:
            left = mid + 1
        elif array[mid] > key:
            right = mid - 1

    return idx


def test(array, key):
    print('----------------------------------------')
    print(array, key)
    print('binarySearch:           {}'.format(binarySearch(array, key)))
    print('binarySearchFirst:      {}'.format(binarySearchFirst(array, key)))
    print('binarySearchLast:       {}'.format(binarySearchLast(array, key)))


if __name__ == '__main__':
    array = [-1, 1, 3, 3, 7, 7, 7, 7, 9, 9]
    for key in range(-2, 11):
        test(array, key)
