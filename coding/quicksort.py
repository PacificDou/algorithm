
def partition(array, start, end):
    pivot = array[end] # cannot be other element, because pivot must be at boundary after partition
    i = start - 1 # array[start..i] will be <= pivot, index is inclusive
    for j in range(start, end + 1):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    return i


def quicksort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quicksort(array, start, p - 1) # cannot be p, otherwise may introduce infinite loop if p equal to boundary
    quicksort(array, p + 1, end)

def quickselect(array, start, end, k):
    if start >= end:
        return array[start]

    p = partition(array, start, end)
    order = p - start + 1
    if order == k:
        return array[p]
    if order < k:
        return quickselect(array, p + 1, end, k - order)
    return quickselect(array, start, p - 1, k)




if __name__ == '__main__':
    array = [3, 2, 1, 5, 0, 4]
    print(array)
    quicksort(array, 0, len(array) - 1)
    print(array)

    array = [5, 4, 3, 2, 1, 0]
    print(array)
    quicksort(array, 0, len(array) - 1)
    print(array)

    array = [0, 1, 2, 3, 4, 5]
    print(array)
    quicksort(array, 0, len(array) - 1)
    print(array)


    array = [5, 4, 3, 2, 1, 0]
    for i in range(len(array)):
        print(quickselect(array[:], 0, len(array) - 1, i + 1))


