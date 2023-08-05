# https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees
# https://halfrost.com/binary_indexed_tree/
# sum of sub-array (start from 1): 1,   1-2,  3,   1-4,  5,   5-6,  7,   1-8,  9,  9-10, 11,  9-12, 13, 13-14, 15, 1-16,
#                                 17, 17-18, 19, 17-20, 21, 21-22, 23, 17-24, 25, 25-26, 27, 25-28, 29, 29-30, 31, 1-31
# i-th bit element (i start from 1): sum array[i-lowbit(i) + 1 ... i]
# i-th array element shown in bit (i start from 1): i, i1 = i + lowbit(i), i2 = i1 + lowbit(i1), i3 = i2 + lowbit(i2), ...

def lowbit(idx):
    return (idx & (-idx))

def build(array):
    n = len(array)
    bit = [0 for i in range(n + 1)]
    for i, num in enumerate(array):
        curIdx = i + 1
        bit[curIdx] += array[i] # bit[idx] is done
        parIdx = curIdx + lowbit(curIdx)
        if parIdx <= n:
            bit[parIdx] += bit[curIdx] # propagate bit[idx] to parent nodes, very important!!!
    return bit

def update(bit, idx, delta):
    n = len(bit)
    while idx < n:
        bit[idx] += delta
        idx += lowbit(idx)

def query(bit, idx):
    ret = 0
    while idx > 0:
        ret += bit[idx]
        idx -= lowbit(idx)
    return ret

def querySingle(bit, idx):
    ret = bit[idx]
    stop = idx - lowbit(idx)
    cur = idx - 1
    while cur != stop:
        ret -= bit[cur]
        cur -= lowbit(cur)
    return ret

if __name__ == '__main__':
    array = [3, 3, 2, 9, 10, 23, 7, 29, 10, 11]
    print(array)

    for i in range(len(array)):
        print('sum(0-{})'.format(i), sum(array[:i + 1]))

    bit = build(array)
    ret = [querySingle(bit, i) for i in range(1, len(bit))]
    print(ret)

    ret = [query(bit, i) for i in range(1, len(bit))]
    print(ret)


