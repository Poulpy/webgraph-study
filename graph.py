import random

class Graph:
    """
    stores adjacency list (hash) :
    vertice : {vertice, vertice}, etc.
    For different implementations, see the wiki article on adjacency lists
    """
    def __init__(self, adjacency_list= {}):
        self.adjacency_list = adjacency_list

    def vertice_count(self):
        """
        Returns the number of vertices
        """
        return len(self.adjacency_list.keys())

    def edge_count(self):
        """
        Returns the number of edges
        """
        total = 0
        vertices_known = []
        for k, v in self.adjacency_list.items():
            for vertice in vertices_known:
                if vertice in v:
                    v.remove(vertice)

            total += len(v)
            vertices_known.append(k)
        return total

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
    def edgar_gilbert_graph(vertice_count):
        """
        creates a random graph, as proposed by Edgar Gilbert
        An edge between each vertice is created with 1/2 probability
        The number of vertices is fixed

        Exceptions: vertice count <= 0
        """

        if vertice_count <= 0:
            return Graph()

        adjacency_list = {}
        edge_appearance_probability = 0.5

        for vertice in range(vertice_count):
            other_vertices = range(vertice_count)
            other_vertices.pop(vertice)
            adjacency_list[vertice] = [i for i in other_vertices if edge_appearance_probability < random.random()]

        return Graph(adjacency_list)

    @staticmethod
    def barabasi_albert_graph(m):
        """
        creates a barabasi-albert graph

        Exception: m <= 0
        """
        if m <= 0:
            return Graph()

        adjacency_list = {0: [1,2],
                          1: [0,2],
                          2: [0,1]}

        for j in range(3, 3 + m):
            sum_of_degrees = float(sum([len(vertices) for _, vertices in adjacency_list.items()]))
            vertice_count = float(len(adjacency_list))
            adjacency_list[j] = []

            for vertice, vertices in adjacency_list.items():
                if (len(vertices) / sum_of_degrees) < random.random():
                    adjacency_list[j].append(vertice)

            #adjacency_list[j] = [i for i in range(vertice_count) if random.random() < (len(adjacency_list[i]) / sum_of_degrees)]

        return Graph(adjacency_list)


    def write(self, filepath):
        """
        write the adjacency list in a TEXT file (not binary)

        Exception: file or path incorrect
        """
        f = open(filepath, "w")
        for vertice, vertices in self.adjacency_list.items():
            f.write(str(vertice) + "," + ",".join(map(str, vertices)))
            f.write("\n")
        f.close()

    @staticmethod
    def read(filepath):
        """
        reads an adjacency list from a TEXT file

        Exception: file or path incorrect
        """
        file = open(filepath)
        adjacency_list = {}

        # Reading from file
        for line in file.readlines():
            vertices = line.rstrip().split(',')
            adjacency_list[vertices[0]] = vertices[1:]

        # closing the file
        file.close()
        return Graph(adjacency_list)
