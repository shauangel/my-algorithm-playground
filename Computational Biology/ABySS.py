import networkx as nx
import matplotlib.pyplot as plt
from enum import Enum

reverse = {"A": "T", "T": "A", "C": "G", "G": "C"}


class BaseValue(Enum):
    A = 0
    C = 1
    G = 2
    T = 3


class ABySS:
    def __init__(self, seq, K):
        self.seq = seq
        self.nodes = set()
        self.edges = []
        self.parallel = {str(i): set() for i in range(K)}
        self.n_cnt = K

    def compute(self, k):
        for i in range(len(self.seq)-k):
            kmer = self.seq[i:i+k]
            prefix = kmer[0:k-1]
            suffix = kmer[1:k]
            self.nodes.add(prefix)
            self.nodes.add(suffix)
            self.edges.append((prefix, suffix))
            h, rv_h = ABySS.kmer2base4(kmer)
            n = (h ^ rv_h) % self.n_cnt
            self.parallel[str(n)].add(kmer)

    @staticmethod
    def kmer2base4(seq):
        hash_val = 0
        rv_hash_val = 0
        seq_len = len(seq)
        for i in range(seq_len-1, -1, -1):
            curr = seq[seq_len-1-i]
            hash_val += BaseValue[curr].value * 4**i
            curr_rv = seq[i]
            rv_hash_val += BaseValue[reverse[curr_rv]].value * 4**i
        return hash_val, rv_hash_val

    def get_adjacency_list(self):
        adj = {node:set() for node in self.nodes}
        for i in self.edges:
            adj[i[0]].add(i[1])
            adj[i[1]].add(i[0])
        return adj

    def display(self):
        graph = nx.Graph(self.edges)
        plt.figure(figsize=(10, 8))
        nx.draw(graph, with_labels=True, node_color="lightblue",
                node_size=300, font_size=10, font_weight="bold", edge_color="gray")
        plt.show()


if __name__ == "__main__":
    with open("test.FASTA", 'r') as f:
        data = f.readlines()
    dbg = ABySS(data[1].replace('\n', ''), 4)
    dbg.compute(3)
    # print(dbg.nodes)
    # print(dbg.edges)
    # dbg.display()
    # h, rv_h = dbg.kmer2base4("ACG")
    print(dbg.parallel)



