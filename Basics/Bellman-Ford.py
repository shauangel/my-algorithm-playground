import math

class BellmanFord:
    def __init__(self, graph):
        self.graph = graph
        self.dist = {node: math.inf for node in graph}
        self.edge = []
        for u in graph:
            for v in graph[u]:
                self.edge.append({"u": u, "v": v, "l": graph[u][v]})
        self.prev = {node: None for node in graph}
        # print(len(self.edge))

    def update(self, u, v, l):
        if self.dist[v] > self.dist[u] + l:
            self.dist[v] = self.dist[u] + l
            self.prev[v] = u

    def bellman_ford(self, s):
        self.dist[s] = 0
        for k in range(len(self.graph)-1):
            for e in self.edge:
                self.update(e['u'], e['v'], e['l'])
            print(self.dist)


if __name__ == "__main__":
    graph = {
        'S': {'A': 3, 'F': 5},
        'A': {'B': 4, 'C': -5},
        'B': {'G': -3, 'H': -4},
        'C': {'D': 7, 'F': -2},
        'D': {},
        'E': {'F': -6, 'H': 4},
        'F': {'D': 3},
        'G': {'I': -1},
        'H': {'G': 2},
        'I': {'H': 1}
    }

    test = BellmanFord(graph)
    test.bellman_ford('S')
    print(test.prev)
    # print(test.dist)