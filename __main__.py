import sys
from graph import Graph

DATA_DIR = "data/"

def create_edgar_gilbert_graph():
    graph = Graph.edgar_gilbert_graph(1000)
    graph.write_parameters(DATA_DIR + "edgar_gilbert_graph.csv")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "eg":
            create_edgar_gilbert_graph()

