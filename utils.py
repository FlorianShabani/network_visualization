import os
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

class Utils:
    @staticmethod
    def get_graphs(path):
        path = Path(path)
        graphs = []
        for filename in os.listdir(path):
            if filename.endswith('.gml'):
                graphs.append(Utils.load_graph(os.path.join(path, filename)))
        return graphs

    @staticmethod
    def load_graph(path):
        ext = os.path.splitext(path)[1].lower()
    
        if ext == '.gml':
            g = nx.read_gml(path, label='id')
            if not g.name:
                g.name = Path(path).stem
            return g
        else:
            raise ValueError(f"Unsupported file type: {ext}")

    @staticmethod
    def time_function(func, *args, **kwargs):
        import time

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        return result, end_time - start_time

    @staticmethod    
    def plot_graph(g, pos, save=None, show=False):
        nx.draw(g, pos)
        if save:
            Path(save).parent.mkdir(parents=True, exist_ok=True)
            plt.savefig(save)
        plt.show()
