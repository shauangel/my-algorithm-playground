"""
Chiba and Nishizeki's Algorithm

Concept:
intersecting the neighborhoods of adjacent vertices
performed in descending order of degree

Input: graph G=(V, E)
Output: A list of triangles
"""
import itertools
import math


test = {
  "1": [2, 3, 7, 10],
  "2": [1, 3, 4, 5],
  "3": [1, 2, 6, 7],
  "4": [2, 5],
  "5": [2, 4, 8, 9],
  "6": [3, 7],
  "7": [3, 6, 1, 10],
  "8": [5, 9],
  "9": [5, 8],
  "10": [1, 7]
}


class K3:
    def __init__(self, G):
        self.adj_list = {node: [str(e) for e in G[node]] for node in G}
        # self.sorted_v = [node[0] for node in sorted(G.items(), key=lambda x: len(x[1]), reverse=True)]
        # print(self.adj_list)

    def triangle_listing(self):
        G = self.adj_list.copy()
        mark = {node: 0 for node in self.adj_list}
        sorted_v = [node[0] for node in sorted(self.adj_list.items(), key=lambda x: len(x[1]), reverse=True)]
        for u in sorted_v[:len(sorted_v)-2]:
            for v in G[u]:
                mark[v] = 1
            for v in G[u]:
                for w in G[v]:
                    if mark[w] == 1:
                        print(f"({u}, {v}, {w})")
                    # print(mark)
                mark[v] = 0
            self.remove_vertex(G, u)

    @staticmethod
    def remove_vertex(G, u):
        del G[u]
        for key, val in G.items():
            if u in val:
                val.remove(u)

    def compute_arboricity(self):
        # Generate edges set
        edges = set()
        for node, neighbors in self.adj_list.items():
            for n in neighbors:
                e = tuple(sorted((node, n)))
                edges.add(e)

        nodes = list(map(str, self.adj_list.keys()))
        arboricity = 0
        for r in range(2, len(nodes) + 1):
            for subset in itertools.combinations(nodes, r):
                subset_set = set(subset)
                edge_count = sum(1 for (u, v) in edges if u in subset_set and v in subset_set)
                value = math.ceil(edge_count / (r - 1))
                print(f"Sub-result: E(U)={edge_count}, |U|={r}, a(subset)={value}")
                arboricity = max(arboricity, value)
        return arboricity



if __name__ == "__main__":
    k3 = K3(test)
    k3.triangle_listing()
    a = k3.compute_arboricity()
    print(a)

