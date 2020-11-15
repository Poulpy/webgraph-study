import sys
import os
from graph import Graph

DATA_DIR = "data/"
PLOTS_DIR = DATA_DIR + "plots/"
RESOURCES_DIR = "resources/"

def generate_edgar_gilbert_graph():
    graph = Graph.edgar_gilbert_graph(500)
    graph.write_edges(RESOURCES_DIR + "edgar_gilbert_graph.csv")

def generate_barabasi_albert_graph():
    graph = Graph.barabasi_albert_graph(500)
    graph.write_edges(RESOURCES_DIR + "barabasi_albert_graph.csv")

def generate_plot(filepath: str):
    graph = Graph.read_edges(filepath)
    filename = os.path.splitext(os.path.basename(filepath))[0] + '.png'
    graph.write_graph(PLOTS_DIR + filename)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "eg":
            generate_edgar_gilbert_graph()
        elif sys.argv[1] == "ba":
            generate_barabasi_albert_graph()
    if len(sys.argv) == 3:
        if sys.argv[1] == "file":
            generate_plot(sys.argv[2])
