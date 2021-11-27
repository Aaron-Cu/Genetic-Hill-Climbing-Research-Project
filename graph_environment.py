# An class for creating Undirected Connected Weighted Graphs of any size.
#
import random
import math
from has_ham_circuit import circuit

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
    # Complexity of O(n^2) for generating a graph
    def __init__(self, vert, upper):
        self.vertices_count = vert

        # Populating the adj_matrix[]*verticies_count 
        # with 1s
        print("Generating Edges..")
        self.__pls_fill_ones_uwu()
        self.print()

        # Removing the edges that are from a node
        # to itself.
        print("Removing Loops..")
        self.__no_loops_pls()
        self.print()

        # Removing edges from the currently 
        # fully connected graph
        print("Applying pattern..")
        self.__apply_pattern()
        self.print()

        # Adding weights to the adj_matrix for
        # all edges.
        print("Adding Weights..")
        self.add_weights(upper)
        self.print()

    # Initializes the adjacency matrix with 1s of size
    # vertices_count
    # Time complexity of O(n^2)
    def __pls_fill_ones_uwu(self):
        self.adj_matrix = [[1 for i in range(self.vertices_count)] 
            for j in range(self.vertices_count)]

    # Removes adjacency matrix edges from a vertex to 
    # itself.
    # Time complexity of O(n^2) basic operation: assignment
    def __no_loops_pls(self):
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if i == j:
                    self.adj_matrix[i][j] = 0

    # Removes edges in such a way to keep
    # to still insure a hamoltonian curcut
    # is possible.
    # Complexity of O(n^2)
    def __apply_pattern(self):
        countOfDel = round_down(0.2 * self.vertices_count)
        print(countOfDel)
        i = 0
        ham = circuit()
        while i < countOfDel:
            v1 = random.randint(0, self.vertices_count-1)
            v2 = random.randint(0, self.vertices_count-1)
            if v1 != v2:
                if self.adj_matrix[v1][v2] != 0:
                    self.adj_matrix[v1][v2] = 0
                    self.adj_matrix[v2][v1] = 0
                    if ham.has_hamiltonian(self, 0):
                        i = i+1
                    else:
                        self.adj_matrix[v1][v2] = 1
                        self.adj_matrix[v2][v1] = 1
            


    # Method for balancing the adjacency matrix of the graph. 
    # The matrix should always be balance since this is
    # an undirected graph.
    # Complexity of O(n^2)
    def balance(self):
        for i in range(len(self.adj_matrix)):
            for j in range(0, i):
                self.adj_matrix[j][i] = self.adj_matrix[i][j]

    # Adds random weights from (0 to upper_bound]
    # Complexity of O(n^2)
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
    # complesity of O(n)
    def get_neighbors(self, vertex):
        arr = []
        for index in range(len(self.adj_matrix[vertex])):
            if self.adj_matrix[vertex][index] != 0:
                arr.append(index)
        return arr

    # Method for fetching an edge weight.
    # Complexity of O(1)
    def get_edge_weight(self, vertex_one, vertex_two):
        return self.adj_matrix[vertex_one][vertex_two]

    # returns true if there exists an edge between
    # any two given verticies.
    # Complexity O(1)
    def is_edge(self, vert1, vert2):
        if self.adj_matrix[vert1][vert2] == 0:
            return False
        return True

    # A built in function for printing the adjacency matrix
    # to the console output.
    # Complexity of O(n^2)
    def print(self):
        print()
        for row in self.adj_matrix:
            print(row)
        print()

    # Can be used to ensure that the graph is balanced
    # complexity of O(n^2)
    def test(self):
        test_bool = True
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix)):
                if self.adj_matrix[i][j] != self.adj_matrix[j][i]:
                    test_bool = False
        return test_bool
