class Graph:
    """
    stores adjacency list (hash) :
    vertice : {vertice, vertice}, etc.
    For different implementations, see the wiki article on adjacency lists
    """
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def vertice_count(self):
        """
        TODO
        """
        pass

    def edge_count(self):
        """
        TODO
        """
        pass

    def maximum_degree(self):
        """
        TODO
        """
        pass

    def average_degree(self):
        """
        TODO
        """
        pass

    def diameter(self):
        """
        TODO
        """
        pass

    def degree_distribution(self):
        """
        TODO
        Displays the distribution of degrees. x axis : degree;
        y axis : frequency
        """
        pass

    @staticmethod
    def edgar_gilbert_graph():
        """
        TODO
        creates a random graph, as proposed by Edgar Gilbert
        """
        pass
    
    @staticmethod
    def barabasi_albert_graph():
        """
        TODO
        creates a barabasi-albert graph
        """
        pass

    def write(self, filepath):
        """
        TODO
        write the adjacency list in a TEXT file (not binary)
        """
        pass

    def read(self, filepath):
        """
        TODO
        reads an adjacency list from a TEXT file
        """
        pass
