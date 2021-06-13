class DisjointSet:
    def __init__(self):
        self.node_to_parent = {}
        self.set_size = {}

    def MakeSet(self, val):
        if val in self.node_to_parent:
            return
        self.node_to_parent[val] = None
        self.set_size[val] = 1

    def Find(self, val):
        if self.node_to_parent[val] == None:
            return val
        self.node_to_parent[val] = self.Find(self.node_to_parent[val])
        return self.node_to_parent[val]

    def FindLoop(self, val):
        p = val
        while self.node_to_parent[p] != None:
            p = self.node_to_parent[p]

        while val != p:
            temp = self.node_to_parent[val]
            self.node_to_parent[val] = p
            val = temp
        return p

    def Union(self, x, y):
        xp = self.Find(x)
        yp = self.Find(y)
        if xp != yp:
            self.node_to_parent[xp] = yp
            self.set_size[yp] += self.set_size[xp]
            del self.set_size[xp]

    def getSets(self):
        sets = {}
        for val, par in self.node_to_parent.items():
            root = self.Find(val)
            if root not in sets:
                sets[root] = set()
            sets[root].add(val)
        return sets


if __name__ == '__main__':
    vertices = [0,1,2,3,4,5,6,7,8,9]
    edges = [[0,1], [1,2], [0,3], [2,4], [2,0], [5,6], [6,7]]

    # enumerate all edges
    dset = DisjointSet()
    for v in vertices:
        dset.MakeSet(v)
    for edge in edges:
        dset.Union(edge[0], edge[1])

    sets = dset.getSets()
    for p, set in sets.items():
        print('Set {} : {}'.format(p, set))
    print(dset.set_size)

