"""
Lu-Ravi ['96]
The Power of Local Optimization: Approximation Algorithms for Maximum-Leaf Spanning Tree
1-LOT, 2-LOT
"""
import time

import matplotlib.pyplot as plt
import networkx as nx
from GraphUtil import MyGraph


class LuRaviLOT:
    # Step 1: Initialize LuRavi
    def __init__(self, mygraph):
        self.mygraph = mygraph
        self.T = mygraph.generate_spanning_tree()

    def get_leaf_cnt(self):
        return self.mygraph.count_leaf(self.T)

    def scored_edge_pairs(self, edge1, edge2):
        # High score for pairs that connect high-degree nodes
        score = (self.mygraph.graph.degree[edge1[0]] + self.mygraph.graph.degree[edge1[1]]) + \
                (self.mygraph.graph.degree[edge2[0]] + self.mygraph.graph.degree[edge2[1]])
        return score

    def get_non_tree_edges(self):
        prioritized_edges = sorted(
            self.mygraph.edges, key=lambda edge: self.mygraph.graph.degree[edge[0]] + self.mygraph.graph.degree[edge[1]], reverse=True
        )
        return [e for e in prioritized_edges if e not in self.T.edges]

    # 1-Change improvement
    def apply_1_change(self, e):
        # Step 1: Make a local tree: T_prime
        T_prime = self.T.copy()
        origin_cnt = self.mygraph.count_leaf(T_prime)
        T_prime.add_edge(*e)

        # Step 2: Remove edge in cycle to find best
        best_edge = ()
        best_cnt = origin_cnt
        for temp in nx.find_cycle(T_prime):
            T_prime.remove_edge(*temp)

            # Check valid tree
            if self.mygraph.is_spanning_tree(T_prime):
                # Count leaf
                prime_cnt = self.mygraph.count_leaf(T_prime)
                if prime_cnt > best_cnt:
                    best_edge = temp
                    best_cnt = prime_cnt
            T_prime.add_edge(*temp)

        # Step 3: If improved, update T and return True
        if best_edge != ():
            T_prime.remove_edges_from([best_edge])
            self.T = T_prime.copy()
            return True
        return False

    # 2-Change improvement
    def apply_2_change(self, e1, e2):
        # Step 1: Make a local tree: T_prime, add 2 edges
        T_prime = self.T.copy()
        best_cnt = self.mygraph.count_leaf(T_prime)
        T_prime.add_edges_from([e1, e2])
        best_edge_pair = []

        # Step 2: Detect Cycle
        all_cycles = list(nx.cycle_basis(T_prime))
        if len(all_cycles) > 1:
            cycle1 = [(all_cycles[0][i], all_cycles[0][(i+1)%len(all_cycles[0])]) for i in range(len(all_cycles[0]))]
            cycle2 = [(all_cycles[1][i], all_cycles[1][(i+1)%len(all_cycles[1])]) for i in range(len(all_cycles[1]))]
        else:
            return "err not enough cycle"

        # Step 3: Iterate through all edges pairs
        for edge1 in cycle1:
            for edge2 in cycle2:
                # Remove edges pair
                T_prime.remove_edges_from([edge1, edge2])

                # Check valid tree
                if self.mygraph.is_spanning_tree(T_prime):
                    prime_cnt = self.mygraph.count_leaf(T_prime)
                    if prime_cnt > best_cnt:
                        best_cnt = prime_cnt
                        best_edge_pair = [edge1, edge2]
                T_prime.add_edges_from([edge1, edge2])

        # Step 3: If improved, update T and return true, o.w. false
        if best_edge_pair:
            T_prime.remove_edges_from(best_edge_pair)
            self.T = T_prime.copy()
            return True
        return False

    # Hybrid 1-LOT, 2-LOT approximation
    def run(self):
        improved = True

        while improved:
            improved = False
            non_tree_edges = self.get_non_tree_edges()
            # 1-LOT Improvement
            for e in non_tree_edges:
                improved = self.apply_1_change(e)
            print("Improved 1-LOT: " + str(improved))

        # 2-LOT Improvement
        improved = True
        while improved:
            improved = False
            non_tree_edges = self.get_non_tree_edges()
            for i in range(len(non_tree_edges)-1):
                for j in range(i+1, len(non_tree_edges)):
                    improved = self.apply_2_change(non_tree_edges[i], non_tree_edges[j])
            print("Improved 2-LOT: " + str(improved))
        print(self.mygraph.count_leaf(self.T))

    def output(self):
        tree_edges = list(self.T.edges)
        out = sorted([tuple(sorted(e)) for e in tree_edges], key=lambda x: (x[0], x[1]))
        return out


if __name__ == "__main__":
    start = time.time()
    g = MyGraph("data/graph2")
    alg = LuRaviLOT(g)
    alg.run()
    end = time.time()
    print("Runtime: " + str(end-start))
    print("Leaf Count: " + str(alg.get_leaf_cnt()))
    print(alg.output())


    plt.figure(figsize=(10, 8))
    nx.draw(alg.T, with_labels=True, node_color="lightblue", node_size=300, font_size=10, font_weight="bold",
            edge_color="gray")
    plt.show()
