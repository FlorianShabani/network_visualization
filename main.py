import gdMetriX as gd # type: ignore
import networkx as nx
from utils import Utils

def quality_measures(g, pos):
    crossings = gd.crossings.crossing_density(g, pos)
    stress = gd.symmetry.stress(g, pos)

def spring_layout(g):
    return Utils.time_function(nx.spring_layout, g, k=0.5, iterations=50)

def fmmm_layout(g):
    return Utils.time_function(nx.kamada_kawai_layout, g)

def main():
    path = "test"
    graphs = Utils.get_graphs(f"graphs/{path}")
    for g in graphs:
        pos, time = spring_layout(g)
        Utils.plot_graph(g, pos, save=f"results/{path}/{g.name}.png")
        pos, time = fmmm_layout(g)
        Utils.plot_graph(g, pos, save=f"results/{path}/{g.name}_fmmm.png")
        q = quality_measures(g, pos)

if __name__ == "__main__":
    main()