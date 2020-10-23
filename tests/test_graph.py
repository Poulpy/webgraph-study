from graph import Graph
import unittest

TEST_DIR = "tests/"

class TestGraph(unittest.TestCase):

    def test_edgar_gilbert_graph(self):
        graph = Graph.edgar_gilbert_graph(10)
        graph = Graph.edgar_gilbert_graph(-1)
        self.assertEqual(graph.adjacency_list, Graph().adjacency_list)
        # graph = Graph.edgar_gilbert_graph(1.2)
        # graph = Graph.edgar_gilbert_graph("a")

    def test_barabasi_albert_graph(self):
        graph2 = Graph.barabasi_albert_graph(3)
        graph2 = Graph.barabasi_albert_graph(-1)
        self.assertEqual(graph2.adjacency_list, Graph().adjacency_list)

    def test_write(self):
        adlist = {0: [1,3], 1: [0], 3: [0]}
        graph = Graph(adlist)
        graph.write(TEST_DIR + "test.txt")
        string_should_be = """0,1,3
1,0
3,0
"""
        f = open(TEST_DIR + "test.txt")
        s = f.read()
        f.close()
        self.assertEqual(string_should_be, s)

    def test_read(self):
        file = open(TEST_DIR + "test.txt", "w")
        file.write("0,1,2")
        file.close()

        graph = Graph.read(TEST_DIR + "test.txt")
        adjacency_list_should_be = {'0': ['1', '2']}
        self.assertEqual(adjacency_list_should_be, graph.adjacency_list)

    def test_edge_count(self):
        adlist = {0: [1,3], 1: [0], 3: [0]}
        graph = Graph(adlist)
        self.assertEqual(graph.edge_count(), 2)
        adlist = {0: [1, 3, 56], 1: [0], 3: [0, 56], 56: [0, 3]}
        graph = Graph(adlist)
        self.assertEqual(graph.edge_count(), 4)
        graph = Graph()
        self.assertEqual(graph.edge_count(), 0)

    def test_maximum_degree(self):
        adlist = {0: [1,3], 1: [0], 3: [0]}
        graph = Graph(adlist)
        self.assertEqual(graph.maximum_degree(), 2)

    def test_vertice_count(self):
        adlist = {0: [1,3], 1: [0], 3: [0]}
        graph = Graph(adlist)
        self.assertEqual(graph.vertice_count(), 3)

    def test_average_degree(self):
        adlist = {0: [1,3], 1: [0], 3: [0]}
        graph = Graph(adlist)
        self.assertEqual(graph.average_degree(), 4.0/3.0)

    def test_degree_distribution(self):
        adlist = {0: [1,3], 1: [0], 3: [0]}
        graph = Graph(adlist)
        distrib = graph.degree_distribution()
        self.assertEqual(distrib[1], 1.0/3.0)
        self.assertEqual(distrib[2], 1.0/6.0)

if  __name__ == '__main__':
    unittest.main()
