# An class for creating Undirected Connected Weighted Graphs of any size.
#
import random
import math


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


class Graphiest:
    verticies_count = None
    adj_matrix = None

    # Class Constructor, Initializes a adjacency matrix 
    # of size n by n specified by input perameters.
    # Input: int vert for the number of verticies in 
    # the desired graph.
    def __init__(self, vert, upper):
        self.verticies_count = vert

        print("Generating Edges..")
        self.__pls_fill_ones_uwu()
        self.print()

        print("Removing Loops..")
        self.__no_loops_pls()
        self.print()

        print("Applying pattern..")
        self.__apply_pattern()
        self.print()

        print("Adding Weights..")
        self.add_weights(upper)
        self.print()

    # Initializes the adjacency matrix with 1s of size
    # verticies_count
    def __pls_fill_ones_uwu(self):
        self.adj_matrix = [[1 for i in range(self.verticies_count)] 
            for j in range(self.verticies_count)]

    # Removes adjacency matrix edges from a vertex to 
    # itself.
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
        self.balance()


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

    # A built in function for printing the adjacency matrix
    #  to the console output.
    def print(self):
        print()
        for row in self.adj_matrix:
            print(row)
        print()



# Code for testing the Class Functions
# Output in the console will be used to verify functionality
print("Creating a Fully Connected Graph of size 5 and weights bound by 100")
G = Graphiest(5, 100)

# TESTING ADDING WEIGHTS
# print("Adding weights bounded to 100")
# G.add_weights(100)  # 100 upper bound test
# G.print()

# TESTING BALANCING
# print("Setting bottom Left to 7")
# G.adj_matrix[4][0] = 7
# G.print()
# print("Balancing Right..")
# G.balance()
# G.print()

print("Fettching neighbors of vertex 2")
print()
print(G.get_neighbors(2))
print()

print("Getting weigt of edge from vertex 2 to 4")
print()
print(G.get_edge_weight(2,4))
print()
