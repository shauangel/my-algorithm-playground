"""
Input: an undirected graph G = (V, E), weight of edges
Output: a minimal spanning tree
"""
vertex = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
    ('A', 'B', 5),
    ('A', 'C', 6),
    ('A', 'D', 4),
    ('B', 'C', 1),
    ('B', 'D', 2),
    ('C', 'D', 2),
    ('C', 'E', 5),
    ('C', 'F', 3),
    ('D', 'F', 4),
    ('E', 'F', 4)
]


class KruskalMST:
    def __init__(self, graph):
        self.edges = sorted(graph['E'], key=lambda x:x[2])
        self.vertex = graph['V']
        self.MST = []

    def find_MST(self):
        def find_set(set_list, n):
            for i in range(len(set_list)):
                if n in set_list[i]:
                    return i
        # Step 1: initialize set and empty A
        A = []
        vertex_set = [{nodes} for nodes in self.vertex]
        # Step 2: sort edges in ascending weight (done in obj init)
        # Step 3: Iterate through all edges
        for e in self.edges:
            u_set = find_set(vertex_set, e[0])
            v_set = find_set(vertex_set, e[1])
            if u_set != v_set:
                vertex_set[u_set] = vertex_set[u_set].union(vertex_set[v_set])
                del vertex_set[v_set]
                A.append(e)
        self.MST = A
        return A


    def find_MST_weight(self):
        return sum(n[2] for n in self.MST)






if __name__ == "__main__":
    G = {"V": vertex, "E": edges}
    kruskal = KruskalMST(G)
    MST = kruskal.find_MST()
    print(MST)
    print(kruskal.find_MST_weight())