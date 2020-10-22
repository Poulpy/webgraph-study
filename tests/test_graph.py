from graph import Graph
import unittest

TEST_DIR = "tests/"

class TestGraph(unittest.TestCase):

    def test_edgar_gilbert_graph(self):
        graph = Graph.edgar_gilbert_graph(10)
        print graph.adjacency_list

    def test_barabasi_albert_graph(self):
        graph2 = Graph.barabasi_albert_graph(3)
        print graph2.adjacency_list

    def test_write(self):
        adlist = {0:[1,3], 1: [0], 3: [0]}
        graph = Graph(adlist)
        graph.write(TEST_DIR + "test.txt")

    def test_read(self):
        file = open(TEST_DIR + "test.txt", "w")
        file.write("0,1,2")
        file.close()

        graph = Graph.read(TEST_DIR + "test.txt")
        print graph.adjacency_list

if  __name__ == '__main__':
    unittest.main()
