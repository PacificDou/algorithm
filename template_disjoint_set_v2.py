class DisjointSet:
    def __init__(self):
        self.node_to_parent = {}
        self.sets = {}

    def MakeSet(self, val):
        if val in self.node_to_parent:
            return
        self.node_to_parent[val] = None
        self.sets[val] = {val}

    def FindRecursion(self, val):
        if self.node_to_parent[val] == None:
            return val
        p = self.Find(self.node_to_parent[val])
        self.node_to_parent[val] = p
        return p

    def Find(self, val):
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
            # set xp as smaller one
            if len(self.sets[xp]) > len(self.sets[yp]):
                xp, yp = yp, xp
            self.node_to_parent[xp] = yp
            self.sets[yp].update(self.sets[xp])
            del self.sets[xp]

    def getSizeOfSet(self, val):
        return len(self.sets[self.Find(val)])


if __name__ == '__main__':
    vertices = [0,1,2,3,4,5,6,7,8,9]
    edges = [[0,1], [1,2], [0,3], [2,4], [2,0], [5,6], [6,7]]

    # enumerate all edges
    dset = DisjointSet()
    for v in vertices:
        dset.MakeSet(v)
    for edge in edges:
        dset.Union(edge[0], edge[1])

    for p, set in dset.sets.items():
        print('Set {}  Size {} : {}'.format(p, dset.getSizeOfSet(p), set))
