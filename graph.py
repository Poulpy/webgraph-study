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

        for vertices in self.adjacency_list.values():
            total += len(vertices)

        return (total / 2)

    def maximum_degree(self):
        """
        Returns the maximum of edges a vertice can have in a graph
        """
        return max([len(i) for i in self.adjacency_list.values()])

    def average_degree(self):
        """
        Returns average degree : total degrees divided by total vertices
        """
        degrees_sum = sum([len(i) for i in self.adjacency_list.values()])
        return degrees_sum / float(self.vertice_count())


    def diameter(self):
        """
        Return the longest path of the shortests path
        """
        shortest_paths = self.floyd_warshall()
        diameter = 0

        for origin, destinations in shortest_paths.items():
            for destination in destinations.values():
                if destination > diameter:
                    diameter = destination

        return diameter

    def degree_distribution(self):
        """
        Returns the distribution of degrees in a hash
        key : degree;
        value : frequency
        """
        degrees = {}
        total_degrees = 2 * self.vertice_count()

        for k in self.adjacency_list.values():
            d = len(k)
            if d in degrees.keys():
                degrees[d] += 1
            else:
                degrees[d] = 1

        for k in degrees.keys():
            degrees[k] = (degrees[k] * 100) / total_degrees

        return degrees

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
            other_vertices = list(range(vertice_count))
            other_vertices.remove(vertice)
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
            sum_of_degrees = float(sum([len(vertices) for vertices in adjacency_list.values()]))
            vertice_count = float(len(adjacency_list))
            adjacency_list[j] = []

            for vertice, vertices in adjacency_list.items():
                probability = len(vertices) / sum_of_degrees
                if probability < random.random():
                    adjacency_list[j].append(vertice)

            #adjacency_list[j] = [i for i in range(vertice_count) if random.random() < (len(adjacency_list[i]) / sum_of_degrees)]

        return Graph(adjacency_list)

    def get_vertices(self):
        vertices = []

        for k, v in self.adjacency_list.items():
            vertices.append(k)
            vertices.extend(v)

        return list(dict.fromkeys(vertices))

    def floyd_warshall(self):
        """
        Floyd Warshall algorithm stores the shortest paths in a matrix
        Credits to Wikipedia article

        Vertices must be INTEGERS because the method is using list
        If using other type (string), then use hash please
        """
        # vertice_count = max(self.adjacency_list.keys())
        # dist = [[float('inf') for i in range(vertice_count + 1)] for j in range(vertice_count + 1)]
        vertice_count = self.vertice_count()
        dist = {}
        vertices = self.get_vertices()

        for v in vertices:
            dist[v] = {}
            for b in vertices:
                dist[v][b] = float('inf')

        for origin, destinations in self.adjacency_list.items():
            dist[origin][origin] = 0
            for destination in destinations:
                dist[origin][destination] = 1


        # for k in range(vertice_count):
        #     for i in range(vertice_count):
        #         for j in range(vertice_count):
        #             if dist[i][j] > dist[i][k] + dist[k][j]:
        #                 dist[i][j] = dist[i][k] + dist[k][j]
        for k in self.adjacency_list.keys():
            for i in self.adjacency_list.keys():
                for j in self.adjacency_list.keys():
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist


    def write_parameters(self, filepath):
        """
        Write parameters in a CSV file
        """
        f = open(filepath, "w")

        f.write(str(self.vertice_count()) + '\t' + str(self.edge_count()) + '\t')
        f.write(str(self.maximum_degree()) + '\t' + str(self.average_degree()))
        f.write('\t' + str(self.diameter()))
        f.write("\n")

        distrib = self.degree_distribution()

        for degree in distrib.keys():
            f.write(str(degree) + '\t')

        f.write("\n")

        for degree in distrib.keys():
            f.write(str(distrib[degree]).replace('.', ',') + '\t')

        f.close()


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

    @staticmethod
    def read_edges(filepath):
        """
        reads edges from a file like this
        edge1,edge2
        """
        file = open(filepath)
        adjacency_list = {}

        # Reading from file
        for line in file.readlines():
            origin, dest = line.rstrip().split(',')
            origin = int(origin)
            dest = int(dest)

            if origin in adjacency_list:
                adjacency_list[origin].append(dest)
            else:
                adjacency_list[origin] = [dest]

            if dest in adjacency_list:
                adjacency_list[dest].append(origin)
            else:
                adjacency_list[dest] = [origin]
        # closing the file
        file.close()
        return Graph(adjacency_list)
