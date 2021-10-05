#An class for creating Undirected Connected Weighted Graphs of any size.
#
class Graphiest:
    verticies = None
    adj_matrix = None

    #Class Constructor, Initializes a adjacency matrix of size n by n specified by input perameters.
    #Input: int vert for the number of verticies in the desired graph.
    def __init__(self, vert):
        verticies = vert
        self.adj_matrix = [[1 for i in range(verticies)] for j in range(verticies)]
        #print(adj_matrix)
        self.print()
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if i == j:
                    self.adj_matrix[i][j] = 0
        self.print()
    
    #Method for balancing the adjacency matrix of the graph. The matrix should always be balance since this is
    #an undirected graph.
    def balance(self):
        for i in range(len(self.adj_matrix)):
            for j in range(0,i):
                    self.adj_matrix[j][i] = self.adj_matrix[i][j]

    #A built in function for printing the adjacency matrix to the console output.
    def print(self):
        print()
        for row in self.adj_matrix:
            print(row)
        print()

#Code for testing the Class Functions
#Output in the console will be used to verify functionality
print("Creating a Fully Connected Graph of size 5")
G = Graphiest(5)
print("Setting bottom Left to 7")
G.adj_matrix[4][0] = 7
G.print()
print("Balancing Right..")
G.balance()
G.print()

