import networkx as nx
import matplotlib.pyplot as plt


def crabGraphs(n, t, graph):
    # A record all connected nodes for each vertex
    cnn={x:[] for x in range(1,n+1)}
    for u,v in graph:
        cnn[u].append(v)
        cnn[v].append(u)
    nodes=set()
    # Sort node by degree (max -> min)
    for u in sorted(cnn, key=lambda s:len(cnn[s]),reverse=True):
        if u not in nodes and len(cnn[u])>=t:
            nodes.add(u)
    for u in sorted(cnn, key=lambda s:len(cnn[s]),reverse=True):
        feetofu=0
        for v in cnn[u]:
            if v not in nodes and feetofu<t:
                nodes.add(v)
                feetofu+=1
    return len(nodes)


"""
1. construct adjancacy matrix
2. BFS and sort nodes by degree (max -> min)
3. 
"""

"""
1
7 2 6
1 2
1 3
2 4
2 5
3 6
3 7
"""
if __name__ == "__main__":
    n = 7
    t = 2
    graph = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7]]
    print(crabGraphs(n, t, graph))
    g = nx.Graph()
    g.add_edges_from(graph)

    plt.figure(figsize=(10, 8))
    nx.draw(g, with_labels=True, node_color="lightblue", node_size=300, font_size=10, font_weight="bold",
            edge_color="gray")
    plt.show()
