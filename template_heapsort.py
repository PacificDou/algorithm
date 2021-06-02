

def heapify(array, heapsize, i):
    maxIdx = i
    leftIdx = 2 * i + 1
    rightIdx = 2 * i + 2

    if leftIdx < heapsize and array[leftIdx] > array[maxIdx]:
        maxIdx = leftIdx
    if rightIdx < heapsize and array[rightIdx] > array[maxIdx]:
        maxIdx = rightIdx

    if maxIdx != i:
        array[i], array[maxIdx] = array[maxIdx], array[i]
        maxHeapify(array, heapsize, maxIdx)


def heapsort(array):
    n = len(array)

    # build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # move the root of heap to end
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)


if __name__ == '__main__':
    array = [3, 2, 1, 5, 0, 4]
    print(array)
    heapsort(array)
    print(array)