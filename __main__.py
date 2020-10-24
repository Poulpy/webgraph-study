import sys
from graph import Graph

DATA_DIR = "data/"

def create_edgar_gilbert_graph():
    graph = Graph.edgar_gilbert_graph(500)
    graph.write_parameters(DATA_DIR + "edgar_gilbert_graph.csv")

def create_barabasi_albert_graph():
    graph = Graph.barabasi_albert_graph(500)
    graph.write_parameters(DATA_DIR + "barabasi_albert_graph.csv")

def read_stanford_graph(filepath):
    graph = Graph.read_edges(filepath)
    graph.write_parameters(DATA_DIR + filepath.split("/")[-1])

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "eg":
            create_edgar_gilbert_graph()
        elif sys.argv[1] == "ba":
            create_barabasi_albert_graph()
    if len(sys.argv) == 3:
        if sys.argv[1] == "read":
            read_stanford_graph(sys.argv[2])
