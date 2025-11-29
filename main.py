import gdMetrix as gd # type: ignore
import networkx as nx
from utils import Utils
from pathlib import Path

def quality_measures(g):
    crossings = gd.crossings.crossings_density(g)
    stress = gd.symmetry.stress(g)

def spring_layout(g):
    return Utils.time_function(nx.spring_layout, g, k=0.5, iterations=50)

def plot_graph(pos, save = False):
    

def main():
    graphs = Utils.get_graphs(Path("graphs/ex_3"))
    for g in graphs:

        q = quality_measures(g)

if __name__ == "__main__":
    main()