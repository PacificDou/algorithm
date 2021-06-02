
def merge(array, start, mid, end, temp):
    i1 = start
    i2 = mid + 1
    i3 = start
    while i1 <= mid and i2 <= end:
        if array[i1] <= array[i2]:
            temp[i3] = array[i1]
            i1 += 1
        else:
            temp[i3] = array[i2]
            i2 += 1
        i3 += 1

    while i1 <= mid:
        temp[i3] = array[i1]
        i1 += 1
        i3 += 1

    while i2 <= end:
        temp[i3] = array[i2]
        i2 += 1
        i3 += 1

    array[start:end + 1] = temp[start:end + 1]


def mergeSort(array, start, end, temp):
    if start >= end:
        return
    mid = (start + end) // 2
    mergeSort(array, start, mid, temp)
    mergeSort(array, mid + 1, end, temp)
    merge(array, start, mid, end, temp)


if __name__ == '__main__':
    array = [3, 2, 1, 5, 0, 4]
    print(array)
    mergeSort(array, 0, len(array) - 1, [0 for i in range(len(array))])
    print(array)