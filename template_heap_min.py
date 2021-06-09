
def heapify(array, i, heapsize):
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

def buildHeap(array):
    heapsize = len(array)
    for i in range(heapsize//2 - 1, -1, -1):
        heapify(array, i, heapsize)

def push(array, item):
    array.append(item)
    i = len(array) - 1
    idxParent = (i - 1) // 2
    while idxParent >= 0 and array[idxParent] > array[i]:
        array[idxParent], array[i] = array[i], array[idxParent]
        i = idxParent
        idxParent = (i - 1) // 2

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

