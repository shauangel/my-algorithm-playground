"""
Chiba and Nishizeki's Algorithm

Concept:
intersecting the neighborhoods of adjacent vertices
performed in descending order of degree

Input: graph G=(V, E)
Output: A list of triangles
"""
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
        mark = {node: 0 for node in self.adj_list}
        sorted_v = [node[0] for node in sorted(self.adj_list.items(), key=lambda x: len(x[1]), reverse=True)]
        for u in sorted_v[:len(sorted_v)-2]:
            for v in self.adj_list[u]:
                mark[v] = 1
            for v in self.adj_list[u]:
                for w in self.adj_list[v]:
                    if mark[w] == 1:
                        print(f"({u}, {v}, {w})")
                    # print(mark)
                mark[v] = 0
            self.remove_vertex(u)

    def remove_vertex(self, u):
        del self.adj_list[u]
        for key, val in self.adj_list.items():
            if u in val:
                val.remove(u)

    def compute_arboricity(self):



if __name__ == "__main__":
    k3 = K3(test)
    k3.triangle_listing()

