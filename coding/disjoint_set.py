class DisjointSet:
    def __init__(self):
        self.father = {}
        self.set_size = {}

    def add(self, x):
        if x in self.father:
            return
        self.father[x] = x
        self.set_size[x] = 1

    def findRecursion(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.findRecursion(self.father[x])
        return self.father[x]

    def find(self, x):
        root = x
        while self.father[root] != root:
            root = self.father[root]

        while self.father[x] != root:
            f = self.father[x]
            self.father[x] = root
            x = f
        return root

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.father[ry] = rx
            self.set_size[rx] += self.set_size.pop(ry)

    def all_sets(self):
        sets = {}
        for x, f in self.father.items():
            root = self.find(f)
            if root not in sets:
                sets[root] = []
            sets[root].append(x)
        return sets


if __name__ == '__main__':
    vertices = [0,1,2,3,4,5,6,7,8,9]
    edges = [[0,1], [1,2], [0,3], [2,4], [2,0], [5,6], [6,7]]

    # enumerate all edges
    dset = DisjointSet()
    for v in vertices:
        dset.add(v)
    for edge in edges:
        dset.union(edge[0], edge[1])

    sets = dset.all_sets()
    for p, set in sets.items():
        print('Set {} : {}'.format(p, set))
    print(dset.set_size)

