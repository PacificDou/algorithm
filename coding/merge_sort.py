
def merge(array, start, mid, end):
    i1 = start
    i2 = mid + 1
    temp = []
    while i1 <= mid and i2 <= end:
        if array[i1] <= array[i2]:
            temp.append(array[i1])
            i1 += 1
        else:
            temp.append(array[i2])
            i2 += 1

    while i1 <= mid:
        temp.append(array[i1])
        i1 += 1

    while i2 <= end:
        temp.append(array[i2])
        i2 += 1

    array[start:end + 1] = temp


def mergeSort(array, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    mergeSort(array, start, mid)
    mergeSort(array, mid + 1, end)
    merge(array, start, mid, end)


if __name__ == '__main__':
    array = [3, 2, 1, 5, 0, 4]
    print(array)
    mergeSort(array, 0, len(array) - 1)
    print(array)

    array = [5, 4, 3, 2, 1, 0]
    print(array)
    mergeSort(array, 0, len(array) - 1)
    print(array)

    array = [0, 1, 2, 3, 4, 5]
    print(array)
    mergeSort(array, 0, len(array) - 1)
    print(array)


