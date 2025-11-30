import gdMetriX as gd # type: ignore
import networkx as nx
from utils import Utils

def quality_measures(g, pos):
    crossings = gd.crossings.crossing_density(g, pos)
    stress = gd.symmetry.stress(g, pos)
    return crossings, stress
def spring_layout(g):
    return Utils.time_function(nx.spring_layout, g, k=0.5, iterations=50)

def fmmm_layout(g):
    return Utils.time_function(nx.kamada_kawai_layout, g)

def process_graph(g, path):
    pos_spring, time_spring = spring_layout(g)
    Utils.plot_graph(g, pos_spring, save=f"results/{path}/{g.name}_spring.png")
    q_spring = quality_measures(g, pos_spring)
    
    pos_fmmm, time_fmmm = fmmm_layout(g)
    Utils.plot_graph(g, pos_fmmm, save=f"results/{path}/{g.name}_fmmm.png")
    q_fmmm = quality_measures(g, pos_fmmm)
    
    print(f"Spring: {q_spring}, FMMM: {q_fmmm}")

def main():
    path = "ex_3"
    graphs = Utils.get_graphs(f"graphs/{path}")
    [process_graph(g, path) for g in graphs]

if __name__ == "__main__":
    main()