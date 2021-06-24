# https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees
# https://halfrost.com/binary_indexed_tree/

def lowbit(idx):
    return (idx & (-idx))

def build(array):
    n = len(array)
    bit = [0 for i in range(n + 1)]
    for i, num in enumerate(array):
        bit[i + 1] += array[i]
        j = i + 1 + lowbit(i + 1)
        if j <= n:
            bit[j] += bit[i + 1]
    return bit

def update(bit, idx, val):
    n = len(bit)
    while idx < n:
        bit[idx] += val
        idx += lowbit(idx)

def query(bit, idx):
    s = 0
    while idx > 0:
        s += bit[idx]
        idx -= lowbit(idx)
    return s

def querySingle(bit, idx):
    s = bit[idx]
    z = idx - lowbit(idx)
    y = idx - 1
    while y != z:
        s -= bit[y]
        y -= lowbit(y)
    return s

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
