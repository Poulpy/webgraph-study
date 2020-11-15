import sys
import os
from graph import Graph

DATA_DIR = "data/"
PLOTS_DIR = DATA_DIR + "plots/"
RESOURCES_DIR = "resources/"
DEFAULT_VERTICE_COUNT = 1000

def generate_edgar_gilbert_graph(vertice_count):
    graph = Graph.edgar_gilbert_graph(vertice_count)
    graph.write_edges(RESOURCES_DIR + "edgar_gilbert_graph.csv")

def generate_barabasi_albert_graph(vertice_count):
    graph = Graph.barabasi_albert_graph(vertice_count)
    graph.write_edges(RESOURCES_DIR + "barabasi_albert_graph.csv")

def generate_plot(filepath: str):
    graph = Graph.read_edges(filepath)
    filename = os.path.splitext(os.path.basename(filepath))[0] + '.png'
    graph.write_graph(PLOTS_DIR + filename)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        vertice_count = DEFAULT_VERTICE_COUNT

        if sys.argv[1] == "graph":
            if len(sys.argv) > 3:
                vertice_count = int(sys.argv[3])

            if sys.argv[2] == "eg":
                generate_edgar_gilbert_graph(vertice_count)
            elif sys.argv[2] == "ba":
                generate_barabasi_albert_graph(vertice_count)

        elif sys.argv[1] == "plot":
            generate_plot(sys.argv[2])
