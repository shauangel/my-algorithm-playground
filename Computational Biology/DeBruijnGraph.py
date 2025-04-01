"""
Definitions:
Let DB(seq, k) as a de bruijn graph representing seq
Let Path(seq, k) as a path consisting |String|-k+1 edges
-> the ith edge labeled by the ith k-mer in seq
-> the ith vertex of path is labeled by (i-1)th k-mer

"""

import networkx as nx
import matplotlib.pyplot as plt


class DeBruijnGraph:
    def __init__(self, seq):
        self.seq = seq
        self.nodes = set()
        self.edges = []

    def compute(self, k):
        for i in range(len(self.seq)-k+1):
            kmer = self.seq[i:i+k]
            prefix = kmer[0:k-1]
            suffix = kmer[1:k]
            self.nodes.add(prefix)
            self.nodes.add(suffix)
            self.edges.append((prefix, suffix))

    def get_adjacency_list(self):
        adj = {node:set() for node in self.nodes}
        for i in self.edges:
            adj[i[0]].add(i[1])
        return adj

    def display(self):
        graph = nx.DiGraph(self.edges)
        plt.figure(figsize=(10, 8))
        nx.draw(graph, with_labels=True, node_color="lightblue",
                node_size=300, font_size=10, font_weight="bold", edge_color="gray")
        plt.show()


if __name__ == "__main__":
    with open("test.FASTA", 'r') as f:
        data = f.readlines()
    test = "CATCAGATAGGA"
    # dbg = DeBruijnGraph(data[1].replace('\n', ''))
    dbg = DeBruijnGraph(test)
    dbg.compute(3)
    print(dbg.nodes)
    print(dbg.edges)
    # dbg.display()

