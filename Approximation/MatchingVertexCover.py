import networkx as nx


def vertex_cover_with_matching(graph):
    # Step 1: Find a maximum matching
    matching = nx.max_weight_matching(graph, maxcardinality=True)

    # Step 2: Add both endpoints of each matching edge to the vertex cover
    vertex_cover = set()
    for u, v in matching:
        vertex_cover.add(u)
        vertex_cover.add(v)

    return vertex_cover


# Example usage
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])
cover = vertex_cover_with_matching(G)
print("Vertex Cover:", cover)
