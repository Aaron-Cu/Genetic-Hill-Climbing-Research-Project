#An application for creating Undirected Fully Connected Weighted Graphs of any size
#


class Graphiest:
    verticies = None
    adj_matrix = None

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
    
    def balance(self):
        for i in range(len(self.adj_matrix)):
            for j in range(0,i):
                    self.adj_matrix[j][i] = self.adj_matrix[i][j]

    def print(self):
        print()
        for row in self.adj_matrix:
            print(row)
        print()


print("Creating a Fully Connected Graph of size 5")
G = Graphiest(5)
print("Setting bottom Left to 7")
G.adj_matrix[4][0] = 7
G.print()
print("Balancing Right..")
G.balance()
G.print()

