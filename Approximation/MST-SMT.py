import networkx as nx
import matplotlib.pyplot as plt
from GraphUtil import MyGraph

class MST_SMT:
    def __init__(self, g, dist, ):
        self.graph =MyGraph(g)
        
        self.T = nx.Graph()