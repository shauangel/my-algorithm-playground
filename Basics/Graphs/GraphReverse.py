import json

from TimedDFS import DFS_time

def reverse_g(graph):
    g_r = {vertex: [] for vertex in graph}
    for u in graph:
        for v in graph[u]:
            g_r[v].append(u)
    for u in g_r:
        g_r[u] = sorted(g_r[u])
    return g_r


if __name__ == "__main__":
    # test = {
    #     1: [2, 7],
    #     2: [],
    #     3: [1, 4, 8],
    #     4: [1, 5],
    #     5: [6, 9],
    #     6: [4, 7],
    #     7: [1],
    #     8: [2, 10],
    #     9: [4],
    #     10: [3, 9]
    # }
    with open("../data/g1.json", "r") as f:
        test = json.load(f)
    g_r = reverse_g(test)
    dfs = DFS_time(g_r)
    dfs.DFS()
    dfs.display()
    print(dfs.post)
    print(sorted(dfs.post, reverse=True))
    print([list(g_r.keys())[dfs.post.index(i)] for i in sorted(dfs.post, reverse=True)])