from __future__ import annotations
from collections import defaultdict
import copy
import matplotlib.pyplot as plt
import random
import sys

class Graph:
    """
    stores adjacency list (hash) :
    vertice : {vertice, vertice}, etc.
    For different implementations, see the wiki article on adjacency lists
    """
    def __init__(self, adjacency_list: dict = {}):
        self.adjacency_list = adjacency_list

    def vertice_count(self) -> int:
        """
        Returns the number of vertices in the graph
        """
        return len(self.adjacency_list.keys())

    def edge_count(self) -> int:
        """
        Returns the number of edges; it's the double of the sum of degrees
        """
        edges = [len(vertices) for vertices in self.adjacency_list.values()]
        return int(sum(edges) / 2)

    def maximum_degree(self) -> int:
        """
        Returns the maximum of edges a vertice can have in a graph
        """
        return max([len(i) for i in self.adjacency_list.values()])

    def average_degree(self) -> int:
        """
        Returns average degree : total degrees divided by total vertices
        """
        degrees_sum = 2 * self.edge_count()
        return degrees_sum / self.vertice_count()


    def diameter(self) -> int:
        """
        Return the longest path of the shortests path
        """
        shortest_paths = self.floyd_warshall()
        diameter = 0

        for destinations in shortest_paths.values():
            for destination in destinations.values():
                if destination > diameter:
                    diameter = destination

        return diameter

    def degree_distribution_as_lists(self) -> list:
        """
        Returns the distribution of degrees in a 2D list
        [d1, d2, ...], [f1, f2, ...]
        """
        distrib = self.degree_distribution()
        degree_count = len(distrib.keys())
        distrib_list = [[0 for i in range(degree_count)] for j in range(2)]
        i = 0

        for degree, freq in distrib.items():
            distrib_list[0][i] = degree
            distrib_list[1][i] = freq
            i += 1

        return distrib_list


    def degree_distribution(self) -> dict:
        """
        Returns the distribution of degrees in a hash
        key : degree;
        value : frequency
        """
        degrees = defaultdict(int)
        total_degrees = self.vertice_count()

        for vertices in self.adjacency_list.values():
            degree = len(vertices)
            degrees[degree] += 1

        for k in degrees.keys():
            degrees[k] = (degrees[k]) / total_degrees

        return degrees

    @staticmethod
    def edgar_gilbert_graph(vertice_count: int) -> Graph:
        """
        creates a random graph, as proposed by Edgar Gilbert
        An edge between each vertice is created with 1/2 probability
        The number of vertices is fixed

        Exceptions: vertice count <= 0
        """

        if vertice_count <= 0:
            return Graph()

        adjacency_list = defaultdict(list)
        edge_appearance_probability = 0.5

        for i in range(vertice_count):
            for j in range(i + 1, vertice_count):
                if random.random() < edge_appearance_probability:
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)

        return Graph(adjacency_list)

    @staticmethod
    def barabasi_albert_graph(m: int) -> Graph:
        """
        creates a barabasi-albert graph

        Exception: m <= 0
        """
        if m <= 0:
            return Graph()

        adjacency_list = defaultdict(list, {0: [1,2], 1: [0,2], 2: [0,1]})

        for j in range(3, 3 + m):
            sum_of_degrees = sum([len(vertices) for vertices in adjacency_list.values()])

            # We want to iterate through all other nodes
            # that means : not the node we're iterating right now (j)
            # and not the nodes which are already connected to j
            nodes = set(adjacency_list.keys()) - { j } - set(adjacency_list[j])

            for node in nodes:
                degree = len(adjacency_list[node])
                probability = degree / sum_of_degrees
                if random.random() < probability:
                    adjacency_list[j].append(node)
                    adjacency_list[node].append(j)

        return Graph(adjacency_list)

    def get_vertices(self) -> list:
        """
        Return all vertices of the graph in a list
        """
        vertices = []

        for k, v in self.adjacency_list.items():
            vertices.append(k)
            vertices.extend(v)

        return list(dict.fromkeys(vertices))

    def get_edges(self) -> list:
        """
        Return edges in a list (no dups)
        [1, 2], [3, 4]
        """
        edge_count = self.edge_count()

        if edge_count == 0:
            return []

        edges = [[] for j in range(edge_count)]
        # dict.copy() doesn't work è.é
        adj_list = copy.deepcopy(self.adjacency_list)
        i = 0

        for node, nodes in adj_list.items():
            for vertex in nodes:
                edges[i] = [node, vertex]
                adj_list[vertex].remove(node)
                i += 1

        return edges

    def floyd_warshall(self) -> dict:
        """
        Floyd Warshall algorithm stores the shortest paths in a matrix
        Credits to Wikipedia article

        Vertices must be INTEGERS because the method is using list
        If using other type (string), then use hash please
        """
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

        for k in self.adjacency_list.keys():
            for i in self.adjacency_list.keys():
                for j in self.adjacency_list.keys():
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist


    def write_parameters(self, filepath: str):
        """
        Write parameters in a CSV file
        """
        original_stdout = sys.stdout

        with open(filepath, 'w') as f:
            sys.stdout = f
            f.write("vertice_count\tedge_count\tmaximum_degree\t")
            f.write("average_degree\n")
            f.write(f"{self.vertice_count()}\t{self.edge_count()}\t")
            f.write(f"{self.maximum_degree()}\t{self.average_degree()}\t")
            # f.write(f"{self.diameter()}\n")
            f.write(f"\n")


            sys.stdout = original_stdout

    def write_edges(self, filepath: str):
        """
        write the list of edges in a TEXT file

        Exception: file or path incorrect
        """
        with open(filepath, 'w') as file:
            for edges in self.get_edges():
                file.write(f"{edges[0]},{edges[1]}\n")


    def write(self, filepath: str):
        """
        write the adjacency list in a TEXT file (not binary)

        Exception: file or path incorrect
        """
        with open(filepath, 'w') as file:
            for vertice, vertices in self.adjacency_list.items():
                vertices_str = ",".join(map(str, vertices))
                file.write(f"{vertice},{vertices_str}\n")

    @staticmethod
    def read(filepath: str) -> Graph:
        """
        reads an adjacency list from a TEXT file

        Exception: file or path incorrect
        """
        adjacency_list = {}

        with open(filepath) as file:
            for line in file.readlines():
                vertices = line.rstrip().split(',')
                adjacency_list[vertices[0]] = vertices[1:]

        return Graph(adjacency_list)

    @staticmethod
    def read_edges(filepath: str) -> Graph:
        """
        reads edges from a file like this
        edge1,edge2
        """
        # defaultdict(list) initializes all values to an empty list
        # pretty convienient for avoiding to search always if the key exists
        adjacency_list = defaultdict(list)

        with open(filepath) as file:

            # Reading from file
            for line in file.readlines():
                origin, dest = line.rstrip().split(',')
                origin = int(origin)
                dest = int(dest)

                adjacency_list[origin].append(dest)
                adjacency_list[dest].append(origin)

        return Graph(adjacency_list)

    def write_graph(self, filepath: str):
        """
        Creates a PNG file containing the plot representing
        the repartition of degrees in the graph
        """
        # getting the data
        distrib = self.degree_distribution_as_lists()

        # create the plot
        plt.bar(distrib[0], distrib[1])
        plt.ylabel('Fréquence')
        plt.xlabel('Degrés')
        plt.title('Graphe de répartition des degrés')

        # create the png file
        plt.savefig(filepath)

    def generate_table_parameters(self, filepath: str):
        fig = plt.figure(dpi = 80)
        ax = fig.add_subplot(1, 1, 1)
        table_data = [
                ['Nombre de sommets', self.vertice_count()],
                ["Nombre d'arcs", self.edge_count()],
                ['Degré maximal', self.maximum_degree()],
                ['Degré moyen', "{0:.2f}".format(self.average_degree())]
        ]

        table = ax.table(cellText=table_data, loc='center')
        table.set_fontsize(14)
        table.scale(1, 4)
        ax.axis('off')

        plt.savefig(filepath)



