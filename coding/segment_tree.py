# PushDownLazy (self.value + children.lazy) similar to: https://halfrost.com/segment_tree/
# at any time, the lazy is NOT already applied to the value
# To get latest value (including lazy): mergeLazy
# Update to latest value (including lazy) and delegate lazy to children: pushDownLazy
# Update to latest value (lazy must be zero) from children: pushUpValue
# there is another type of PushDownLazy (children.value + children.lazy): https://blog.csdn.net/zearot/article/details/48299459


class Node:
    def __init__(self, left, right, mid, val, leftChild=None, rightChild=None):
        self.left = left
        self.right = right
        self.mid = mid
        self.isLeaf = left == right

        self.val = val
        self.lazy = 0

        self.leftChild = leftChild
        self.rightChild = rightChild

    def mergeLazy(self):
        return self.val + (self.right - self.left + 1) * self.lazy

    def pushDownLazy(self):
        if self.lazy != 0:
            self.val = self.mergeLazy()
            if not self.isLeaf:
                self.leftChild.lazy += self.lazy
                self.rightChild.lazy += self.lazy
            self.lazy = 0

    def pushUpValue(self):
        if not self.isLeaf:
            self.val = self.leftChild.mergeLazy() + self.rightChild.mergeLazy()
        return self.val


def build(array, left, right):
    if left == right:
        return Node(left, left, left, array[left])

    # init node
    mid = (left + right) // 2
    leftChild = build(array, left, mid)
    rightChild = build(array, mid + 1, right)
    node = Node(left, right, mid, 0, leftChild, rightChild)

    # update node value
    node.pushUpValue()
    return node



def updateSingle(node, idx, delta):
    # outside of the interval
    if idx < node.left or idx > node.right:
        return

    # leaf node
    if node.isLeaf:
        node.val += delta
        return

    node.pushDownLazy()

    # update left OR right sub interval
    if idx <= node.mid:
        updateSingle(node.leftChild, idx, delta)
    else:
        updateSingle(node.rightChild, idx, delta)

    # update node value
    node.pushUpValue()


def updateV2(node, updateLeft, updateRight, delta):
    # can switch the step "PushDownLazy" and "CompletelyInsideInterval" like in function updateV2
    # push down lazy
    node.pushDownLazy()

    # case1: only update lazy if fall inside the update interval
    # completely inside the update interval
    if updateLeft <= node.left and node.right <= updateRight:
        node.lazy += delta
        return

    # case2: only partial interval need to be updated
    # update left OR/AND right sub interval
    if updateLeft <= node.mid:
        updateV2(node.leftChild, updateLeft, updateRight, delta)
    if updateRight > node.mid:
        updateV2(node.rightChild, updateLeft, updateRight, delta)

    # update node value
    node.pushUpValue()


def update(node, updateLeft, updateRight, delta):
    # case1: only update lazy if fall inside the update interval
    # completely inside the update interval
    if updateLeft <= node.left and node.right <= updateRight:
        node.lazy += delta
        return

    # push down lazy
    node.pushDownLazy()

    # case2: only partial interval need to be updated
    # update left OR/AND right sub interval
    if updateLeft <= node.mid:
        update(node.leftChild, updateLeft, updateRight, delta)
    if updateRight > node.mid:
        update(node.rightChild, updateLeft, updateRight, delta)

    # update node value
    node.pushUpValue()

def query(node, queryLeft, queryRight):
    # case1: full interval
    # completely inside the query interval
    if queryLeft <= node.left and node.right <= queryRight:
        return node.mergeLazy()

    # push down lazy
    node.pushDownLazy()

    # case2: partial interval
    # accumulate result from left OR/AND right sub interval
    ret = 0
    if queryLeft <= node.mid:
        ret += query(node.leftChild, queryLeft, queryRight)
    if queryRight > node.mid:
        ret += query(node.rightChild, queryLeft, queryRight)

    return ret

def queryV2(node, queryLeft, queryRight):
    # push down lazy
    node.pushDownLazy()

    # case1: full interval
    # completely inside the query interval
    if queryLeft <= node.left and node.right <= queryRight:
        return node.val

    # case2: partial interval
    # accumulate result from left OR/AND right sub interval
    ret = 0
    if queryLeft <= node.mid:
        ret += queryV2(node.leftChild, queryLeft, queryRight)
    if queryRight > node.mid:
        ret += queryV2(node.rightChild, queryLeft, queryRight)

    return ret

def querySingle(node, idx): # idx must be valid
    # push down lazy
    node.pushDownLazy()

    # completely inside the query interval
    if node.isLeaf:
        return node.val

    # query left OR right sub interval
    ret = None
    if idx <= node.mid:
        ret = querySingle(node.leftChild, idx)
    else:
        ret = querySingle(node.rightChild, idx)

    return ret





if __name__ == '__main__':
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # init segment tree
    root = build(array, 0, len(array) - 1)
    print(array)
    print([querySingle(root, i) for i in range(len(array))])
    for rg in [(0, 3), (2, 5), (1, 4), (6, 9)]:
        print(sum(array[rg[0]:rg[1] + 1]), query(root, rg[0], rg[1]))


    # single element update
    for op in [(3, 5), (7, 3), (0, -4), (3, 0), (8, -2)]:
        idx, delta = op
        array[idx] += delta
        updateSingle(root, idx, delta)

    print(array)
    print([querySingle(root, i) for i in range(len(array))])
    for rg in [(0, 3), (2, 5), (1, 4), (6, 9)]:
        print(sum(array[rg[0]:rg[1] + 1]), query(root, rg[0], rg[1]))


    # interval update
    for op in [(0, 4, 3), (0, 1, 2), (0, 2, -4), (3, 4, 3), (0, 4, 7), (8, 9, 5)]:
        i, j, delta = op
        for idx in range(i, j + 1):
            array[idx] += delta
        update(root, i, j, delta)

    print(array)
    print([querySingle(root, i) for i in range(len(array))])
    for rg in [(0, 2), (1, 3), (0, 4), (1, 4), (2, 4)]:
       print(sum(array[rg[0]:rg[1] + 1]), query(root, rg[0], rg[1]))



    # single element update
    for op in [(3, 5), (7, 3), (0, -4), (3, 0), (8, -2)]:
        idx, delta = op
        array[idx] += delta
        updateSingle(root, idx, delta)

    print(array)
    print([querySingle(root, i) for i in range(len(array))])
    for rg in [(0, 3), (2, 5), (1, 4), (6, 9)]:
        print(sum(array[rg[0]:rg[1] + 1]), query(root, rg[0], rg[1]))


