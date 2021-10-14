# An class for creating Undirected Connected Weighted Graphs of any size.
#
import random
import math


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


class Graphiest:
    vertices_count = None
    adj_matrix = None

    # Class Constructor, Initializes a adjacency matrix 
    # of size n by n specified by input perameters.
    # Input: int vert for the number of vertices in 
    # the desired graph.
    def __init__(self, vert, upper):
        self.vertices_count = vert

        print("Generating Edges..")
        self.__pls_fill_ones_uwu()
        self.print()

        print("Removing Loops..")
        self.__no_loops_pls()
        self.print()

        ##print("Applying pattern..")
        ##self.__apply_pattern()
        ##self.print()

        print("Adding Weights..")
        self.add_weights(upper)
        self.print()

    # Initializes the adjacency matrix with 1s of size
    # vertices_count
    def __pls_fill_ones_uwu(self):
        self.adj_matrix = [[1 for i in range(self.vertices_count)] 
            for j in range(self.vertices_count)]

    # Removes adjacency matrix edges from a vertex to 
    # itself.
    # complexity of O(n^2) basic operation: assignment
    def __no_loops_pls(self):
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if i == j:
                    self.adj_matrix[i][j] = 0

    #
    #
    def __apply_pattern(self):
        for i in range(len(self.adj_matrix)):
            for j in range(0, i):
                if (i)%2 == 0 and (j)%2 == 0:
                    self.adj_matrix[i][j] = 0
                    self.adj_matrix[j][i] = 0


    # Method for balancing the adjacency matrix of the graph. 
    # The matrix should always be balance since this is
    # an undirected graph.
    def balance(self):
        for i in range(len(self.adj_matrix)):
            for j in range(0, i):
                self.adj_matrix[j][i] = self.adj_matrix[i][j]

    # Adds random weights from (0 to upper_bound]
    def add_weights(self, upper_bound):
        for i in range(len(self.adj_matrix)):
            for j in range(0, i):
                # add some random value
                if self.adj_matrix[i][j] != 0:
                    self.adj_matrix[i][j] = round_down(
                        upper_bound - (random.random() * upper_bound)
                        , 4)  # rand(not 0, to upperbound)
                    self.adj_matrix[j][i] = self.adj_matrix[i][j]

    # Method for fetching a list of the neighbors for any
    # given vertex.
    def get_neighbors(self, vertex):
        arr = []
        for index in range(len(self.adj_matrix[vertex])):
            if self.adj_matrix[vertex][index] != 0:
                arr.append(index)
        return arr

    #Method for fetching an edge weight.
    #
    def get_edge_weight(self, vertex_one, vertex_two):
        return self.adj_matrix[vertex_one][vertex_two]

    #
    #
    def is_edge(self, vert1, vert2):
        if self.adj_matrix[vert1][vert2] == 0:
            return False
        return True

    # A built in function for printing the adjacency matrix
    # to the console output.
    def print(self):
        print()
        for row in self.adj_matrix:
            print(row)
        print()

    # Can be used to ensure that the graph is balanced
    # 
    def test(self):
        test_bool = True
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix)):
                if self.adj_matrix[i][j] != self.adj_matrix[j][i]:
                    test_bool = False
        return test_bool
