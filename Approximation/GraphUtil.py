import random
import matplotlib.pyplot as plt
import networkx as nx
import re


def read_graph(fn):
    with open(fn, 'r') as f:
        data = f.readlines()
        f.close()

    new_graph = nx.Graph()
    for e in data:
        vertices = re.findall(r'[0-9]+', e)
        if len(vertices) > 1:
            new_graph.add_edge(int(vertices[0]), int(vertices[1]))
    return new_graph


class MyGraph:
    def __init__(self, fn="", data=[]):
        if fn != "":
            self.graph = read_graph(fn)
        else:
            self.graph = nx.Graph()
            self.graph.add_edges_from(data)
        self.nodes = list(self.graph.nodes)
        self.edges = list(self.graph.edges)
        self.tree = []

    def dfs(self, node, visited):
        visited.add(node)
        for neighbor in self.graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                self.tree.append(tuple(sorted((node, neighbor))))
                self.dfs(neighbor, visited)

    def generate_spanning_tree(self):
        self.tree = []
        prioritized_nodes = sorted(
            self.graph.nodes, key=lambda nodes: self.graph.degree[nodes], reverse=True
        )
        self.dfs(prioritized_nodes[0], set())
        new_tree = nx.Graph()
        new_tree.add_edges_from(self.tree)
        return new_tree

    def count_leaf(self, tree):
        cnt = 0
        for n in self.nodes:
            # leaf has degree 1
            if tree.degree(n) == 1:
                cnt += 1
        return cnt

    def is_spanning_tree(self, tree):
        # print(len(tree.edges))
        # print(len(self.nodes))
        # print(list(nx.isolates(tree)))
        if len(tree.edges) == len(self.nodes)-1:
            if not list(nx.isolates(tree)):
                if len(list(nx.cycle_basis(tree))) == 0:
                    return True
        return False


if __name__ == "__main__":
    fn = "data/graph1"
    g = MyGraph(fn)
    test = nx.Graph()
    test.add_edges_from(g.generate_spanning_tree().edges)
    cnt = g.count_leaf(test)
    print(cnt)

    # Draw the graph
    # plt.figure(figsize=(10, 8))
    # nx.draw(test, with_labels=True, node_color="lightblue", node_size=300, font_size=10, font_weight="bold",
    #         edge_color="gray")
    # plt.title("Random Graph with Complex Cycles", fontsize=16)
    # plt.show()

