"""
Find SCCs by DFS
"""
import numpy as np

adj_list = {
    1: [2, 4],
    2: [1, 4, 10],
    3: [6, 9],
    4: [1, 2],
    5: [],
    6: [3, 7],
    7: [6, 8],
    8: [7, 9],
    9: [3, 8],
    10: [2]
}

class DFS_color:
    def __init__(self, graph):
        self.visited = [0]*len(graph)+1
        self.graph = graph

    @staticmethod
    def id_maps(i):
        if i is int:
            return i
        else:
            return ord(i)-ord('A')+1

    def explore(self, i, cc):
        idx = DFS_color.id_maps(i)
        self.visited[idx] = cc
        print("Visit "+str(i) + ": " + str(self.visited[1:]))
        for u in self.graph[i]:
            u_id = DFS_color.id_maps(u)
            if self.visited[u_id] == 0:
                self.explore(u, cc)

    def DFS(self, order=[]):
        cc = 0
        if len(order) == 0:
            order = list(self.graph.keys())
        for i in order:
            if self.visited[i] == 0:
                cc += 1
                self.explore(i, cc, self.visited)
        print(self.visited[1:])


# DFS(list(range(1, 11)))
