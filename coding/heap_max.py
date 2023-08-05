
# top down heapify
def heapifyTopDownRecursion(array, i, heapsize):
    idxL = 2 * i + 1
    idxR = 2 * i + 2
    maxIdx = i
    if idxL < heapsize and array[maxIdx] < array[idxL]:
        maxIdx = idxL
    if idxR < heapsize and array[maxIdx] < array[idxR]:
        maxIdx = idxR
    if maxIdx != i:
        array[maxIdx], array[i] = array[i], array[maxIdx]
        heapifyTopDownRecursion(array, maxIdx, heapsize)

# top down heapify
def heapifyTopDown(array, i, heapsize):
    while True:
        idxL = 2 * i + 1
        idxR = 2 * i + 2
        maxIdx = i
        if idxL < heapsize and array[maxIdx] < array[idxL]:
            maxIdx = idxL
        if idxR < heapsize and array[maxIdx] < array[idxR]:
            maxIdx = idxR
        if maxIdx != i:
            array[maxIdx], array[i] = array[i], array[maxIdx]
            i = maxIdx
        else:
            break

# bottom up heapify
def heapifyBottomUp(array, i):
    iP = (i - 1) // 2
    while iP >= 0 and array[i] > array[iP]:
        array[i], array[iP] = array[iP], array[i]
        i = iP
        iP = (i - 1) // 2

def push(array, item):
    array.append(item)
    heapifyBottomUp(array, len(array) - 1)

def pop(array):
    ret = array[0]
    array[0] = array[-1]
    del array[-1]
    heapifyTopDown(array, 0, len(array))
    return ret

def delete(array, i, heapsize):
    array[i] = array[-1]
    del array[-1]
    if i == len(array):
        return
    heapifyBottomUp(array, i)
    heapifyTopDown(array, i, heapsize - 1)


def heapSort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapifyTopDown(array, i, n)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapifyTopDown(array, 0, i)
    return array



if __name__ == '__main__':
    array = [6, 3, 8, 1, 1, 2, 9, 7, 7, 3]
    print(heapSort(array.copy()))

    heap = []
    for num in array:
        push(heap, num)
    n = len(heap)
    print([pop(heap) for i in range(n)])

    heap = []
    for num in array:
        push(heap, num)
    print(heap)
    print(heap)
    delete(heap, 3, len(heap))
    n = len(heap)
    print([pop(heap) for i in range(n)])


