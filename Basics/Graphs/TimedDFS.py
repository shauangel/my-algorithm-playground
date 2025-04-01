"""
DFS with timing (pre, post)
"""

g_list = {
    "A": ["B", "D"],
    "B": ["C", "E"],
    "C": ["F"],
    "D": ["H"],
    "E": ["A", "H"],
    "F": ["I"],
    "G": ["D"],
    "H": ["F", "G", "I"],
    "I": ["H"]
}


class DFS_time:


    def __init__(self, graph):
        self.graph = graph
        self.TIME = 0
        self.pre = [0] * len(graph)
        self.post = [0] * len(graph)
        self.visited = [0] * len(graph)

    @staticmethod
    def id_maps(i):
        if type(i) is int:
            idx = i-1
        else:
            idx = ord(i)-ord('A')
        return idx
    def explore(self, i):
        self.TIME += 1
        idx = DFS_time.id_maps(i)
        self.visited[idx] = 1
        self.pre[idx] = self.TIME
        for u in self.graph[i]:
            u_id = DFS_time.id_maps(u)
            if self.visited[u_id] == 0:
                self.explore(u)
        self.TIME += 1
        self.post[idx] = self.TIME

    def DFS(self):
        for i in list(self.graph.keys()):
            i_id = DFS_time.id_maps(i)
            if self.visited[i_id] == 0:
                self.explore(i)

    def display(self):
        for v in list(self.graph.keys()):
            v_id = DFS_time.id_maps(v)
            print(f"{v}: ({self.pre[v_id]}, {self.post[v_id]})")


# dfs = DFS_time(g_list)
# dfs.DFS()
# dfs.display()