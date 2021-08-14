
# top down heapify
def heapifyTopDownRecursion(array, i, heapsize):
    idxL = 2 * i + 1
    idxR = 2 * i + 2
    minIdx = i
    if idxL < heapsize and array[minIdx] > array[idxL]:
        minIdx = idxL
    if idxR < heapsize and array[minIdx] > array[idxR]:
        minIdx = idxR
    if minIdx != i:
        array[minIdx], array[i] = array[i], array[minIdx]
        heapify(array, minIdx, heapsize)

# top down heapify
def heapifyTopDown(array, i, heapsize):
    while True:
        idxL = 2 * i + 1
        idxR = 2 * i + 2
        minIdx = i
        if idxL < heapsize and array[minIdx] > array[idxL]:
            minIdx = idxL
        if idxR < heapsize and array[minIdx] > array[idxR]:
            minIdx = idxR
        if minIdx != i:
            array[minIdx], array[i] = array[i], array[minIdx]
            i = minIdx
        else:
            break

# bottom up heapify
def heapifyBottomUp(array, i):
    iP = (i - 1) // 2
    while iP >= 0 and array[i] < array[iP]:
        array[i], array[iP] = array[iP], array[i]
        i = iP
        iP = (i - 1) // 2

def buildHeap(array):
    heapsize = len(array)
    for i in range(heapsize//2 - 1, -1, -1):
        heapifyTopDown(array, i, heapsize)

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
    heapsize -= 1
    iP = (i - 1) // 2
    if iP >= 0 and array[i] < array[iP]:
        heapifyBottomUp(array, i)
    else:
        heapifyTopDown(array, i, heapsize)

def heapSort(array):
    buildHeap(array)
    n = len(array)
    ret = [pop(array) for i in range(n)]
    return ret


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
    delete(heap, 3, len(heap))
    n = len(heap)
    print([pop(heap) for i in range(n)])

