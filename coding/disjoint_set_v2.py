class Node:
    def __init__(self, val):
        self.val = val
        self.p = None
        self.rank = 0

def MakeSet(val):
    node = Node(val)
    node.rank = 0
    node.p = node
    return node

def FindRecursion(node):
    if node.p != node:
        node.p = Find(node.p)
    return node.p

def Find(node):
    p = node.p
    while p.p != p:
        p = p.p

    while node != p:
        temp = node.p
        node.p = p
        node = temp
    return node.p

def Union(x, y):
    xp = Find(x)
    yp = Find(y)
    if xp.rank > yp.rank:
        yp.p = xp
    elif xp.rank < yp.rank:
        xp.p = yp
    else:
        xp.p = yp
        yp.rank += 1


if __name__ == '__main__':
    vertices = [0,1,2,3,4,5,6,7,8,9]
    edges = [[0,1], [1,2], [0,3], [2,4], [2,0], [5,6], [6,7]]

    # enumerate all edges
    nodes = {v:MakeSet(v) for v in vertices}
    for edge in edges:
        Union(nodes[edge[0]], nodes[edge[1]])

    # connected parts
    sets = {}
    for node in nodes.values():
        p = node.p
        if p not in sets:
            sets[p] = set()
        sets[p].add(node)

    for p, set in sets.items():
        print('Set {} : {}'.format(p.val, [n.val for n in set]))


