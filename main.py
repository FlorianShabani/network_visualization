import gdMetriX as gd # type: ignore
import networkx as nx
from utils import Utils

def quality_measures(g, pos):
    end = gd.symmetry.even_neighborhood_distribution(g, pos)
    stress = gd.symmetry.stress(g, pos)
    return end, stress
def spring_layout(g):
    return Utils.time_function(nx.spring_layout, g, iterations=1000)

def fmmm_layout(g):
    return Utils.time_function(nx.kamada_kawai_layout, g)

def process_graph(g, path):
    pos_spring, time_spring = spring_layout(g)
    Utils.plot_graph(g, pos_spring, save=f"results/{path}/{g.name}_spring.png", node_size=50)
    q_spring = quality_measures(g, pos_spring)
    
    pos_fmmm, time_fmmm = fmmm_layout(g)
    Utils.plot_graph(g, pos_fmmm, save=f"results/{path}/{g.name}_fmmm.png", node_size=50)
    q_fmmm = quality_measures(g, pos_fmmm)
    
    print(f"{g.name:30} | {q_spring[0]:24.4f} | {q_spring[1]:13.4f} | {time_spring:11.4f} | {q_fmmm[0]:22.4f} | {q_fmmm[1]:11.4f} | {time_fmmm:9.4f}")

def main():
    path = "ex_3"
    graphs = Utils.get_graphs(f"graphs/{path}")
    print(f"{'Graph Name':30} | {'Spring END':24} | {'Spring Stress':13} | {'Spring Time':11} | {'FMMM END':22} | {'FMMM Stress':11} | {'FMMM Time':9}")
    print("-" * 140)
    [process_graph(g, path) for g in graphs]

if __name__ == "__main__":
    main()