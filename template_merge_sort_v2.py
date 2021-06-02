
def merge(array, start, mid, end):
    maxN = max(array[start:end + 1]) + 1
    arrayL = array[start:mid + 1] + [maxN]
    arrayR = array[mid + 1:end + 1] + [maxN]
    iL = 0
    iR = 0
    for i in range(start, end + 1):
        if arrayL[iL] <= arrayR[iR]:
            array[i] = arrayL[iL]
            iL += 1
        else:
            array[i] = arrayR[iR]
            iR += 1

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