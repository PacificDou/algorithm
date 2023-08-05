import collections

class GraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
    def __str__(self):
        return '{}-->{}'.format(self.label, [i.label for i in self.neighbors])


def topologicalSortBFS(nodes):
    ret = []

    # calculate indegree
    indegree = collections.defaultdict(int)
    for node in nodes:
        for nb in node.neighbors:
            indegree[nb] += 1

    # BFS traversal
    queue = collections.deque()
    for node in nodes:
        if indegree[node] == 0:
            queue.append(node)
    while len(queue) > 0:
        node = queue.popleft()
        ret.append(node)
        for nb in node.neighbors:
            indegree[nb] -= 1
            if indegree[nb] == 0:
                queue.append(nb)

    return ret


def topologicalSortDFS(nodes):
    ret = []

    # calculate indegree
    indegree = {}
    for node in nodes:
        indegree[node] = 0
    for node in nodes:
        for nb in node.neighbors:
            indegree[nb] += 1

    # DFS traversal
    stack = collections.deque()
    for node, degree in indegree.items():
        if degree == 0:
            stack.append(node)
    while len(stack) > 0:
        node = stack.pop()
        ret.append(node)
        for nb in node.neighbors:
            indegree[nb] -= 1
            if indegree[nb] == 0:
                stack.append(nb)

    return ret


if __name__ == '__main__':
    graph = [0, 1, 2, 3, '#', 1,4, '#', 2,4,5, '#', 3,4,5, '#', 4, '#', 5]
    nodes = {}
    n = len(graph)
    i = 0
    while i < n:
        if graph[i] not in nodes:
            nodes[graph[i]] = GraphNode(graph[i])
        j = i + 1
        while j < n and graph[j] != '#':
            if graph[j] not in nodes:
                nodes[graph[j]] = GraphNode(graph[j])
            nodes[graph[i]].neighbors.append(nodes[graph[j]])
            j += 1
        i = j + 1

    nodes = list(nodes.values())
    print('---------- Graph ----------')
    for n in nodes:
        print(str(n))

    nd = topologicalSortBFS(nodes)
    print('---------- Sort by BFS ----------')
    for n in nd:
        print(str(n))

    nd = topologicalSortDFS(nodes)
    print('---------- Sort by DFS ----------')
    for n in nd:
        print(str(n))


