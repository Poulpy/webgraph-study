from graph import Graph

if __name__ == "__main__":
    graph = Graph.edgar_gilbert_graph(10)
    print graph.adjacency_list

    graph2 = Graph.barabasi_albert_graph(3)
    print graph2.adjacency_list

    graph2.write("test.txt")
    graph3 = Graph.read("test.txt")
    print graph3.adjacency_list