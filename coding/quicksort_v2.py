
def partition(array, start, end):
    mid = (start + end) // 2
    pivot = array[mid]
    left = start
    right = end
    while left <= right:
        while left <= right and array[left] < pivot:
            left += 1
        while left <= right and array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return right, left # left - right == 1 or 2 (like [0, 1])


def quicksort(array, start, end):
    if start >= end:
        return
    p1, p2 = partition(array, start, end)
    quicksort(array, start, p1)
    quicksort(array, p2, end)


if __name__ == '__main__':
    array = [3, 2, 1, 5, 0, 4]
    print(array)
    quicksort(array, 0, len(array) - 1)
    print(array)
