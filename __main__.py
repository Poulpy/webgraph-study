import sys
import os
from graph import Graph

DATA_DIR = "data/"
PLOTS_DIR = DATA_DIR + "plots/"

def generate_edgar_gilbert_plot():
    graph = Graph.edgar_gilbert_graph(500)
    graph.write_graph(PLOTS_DIR + "edgar_gilbert_graph.png")

def generate_barabasi_albert_plot():
    graph = Graph.barabasi_albert_graph(500)
    graph.write_graph(PLOTS_DIR + "barabasi_albert_graph.png")

def generate_stanford_plot(filepath):
    graph = Graph.read_edges(filepath)
    filename = os.path.splitext(os.path.basename(filepath))[0] + '.png'
    graph.write_graph(PLOTS_DIR + filename)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "eg":
            generate_edgar_gilbert_plot()
        elif sys.argv[1] == "ba":
            generate_barabasi_albert_plot()
    if len(sys.argv) == 3:
        if sys.argv[1] == "file":
            generate_stanford_plot(sys.argv[2])
