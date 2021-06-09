
def heapify(array, i, heapsize):
    idxL = 2 * i + 1
    idxR = 2 * i + 2
    maxIdx = i
    if idxL < heapsize and array[maxIdx] < array[idxL]:
        maxIdx = idxL
    if idxR < heapsize and array[maxIdx] < array[idxR]:
        maxIdx = idxR
    if maxIdx != i:
        array[maxIdx], array[i] = array[i], array[maxIdx]
        heapify(array, maxIdx, heapsize)

def buildHeap(array):
    heapsize = len(array)
    for i in range(heapsize//2 - 1, -1, -1):
        heapify(array, i, heapsize)

def push(array, item):
    array.append(item)
    i = len(array) - 1
    iP = (i - 1) // 2
    while iP >= 0 and array[iP] < array[i]:
        array[iP], array[i] = array[i], array[iP]
        i = iP
        iP = (i - 1) // 2

def pop(array):
    ret = array[0]
    array[0] = array[-1]
    del array[-1]
    heapify(array, 0, len(array))
    return ret


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

