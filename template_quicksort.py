
def partition(array, start, end):
    pivot = array[end] # cannot be other element, otherwise the break point may at boundary
    i = start - 1 # array[start..i] will be <= pivot, index is inclusive
    for j in range(start, end + 1):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    return i


def QuickSort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    QuickSort(array, start, p - 1) # cannot be p, otherwise may introduce infinite loop if p equal to boundary
    QuickSort(array, p + 1, end)


if __name__ == '__main__':
    array = [3, 2, 1, 5, 0, 4]
    print(array)
    QuickSort(array, 0, len(array) - 1)
    print(array)
