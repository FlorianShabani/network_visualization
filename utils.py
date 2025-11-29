import os
import networkx as nx

class Utils:
    @staticmethod
    def get_graphs(path):
        graphs = []
        for filename in os.listdir(path):
            if filename.endswith('.gml'):
                graphs.append(Utils.load_graph(os.path.join(path, filename)))
        return graphs

    @staticmethod
    def load_graph(path):
        ext = os.path.splitext(path)[1].lower()
    
        if ext == '.gml':
            return nx.read_gml(path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")

    @staticmethod
    def save_graph(g, path):
        ext = os.path.splitext(path)[1].lower()

    @staticmethod
    def time_function(func, *args, **kwargs):
        import time

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        return result, end_time - start_time