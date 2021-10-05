#An application for creating Undirected Fully Connected Weighted Graphs of any size
#


class Graphiest:
    verticies = None
    adj_matrix = None

    def __init__(self, vert):
        verticies = vert
        self.adj_matrix = [[1 for i in range(verticies)] for j in range(verticies)]
        #print(adj_matrix)
        for row in self.adj_matrix:
            print(row)
        print()
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if i == j:
                    self.adj_matrix[i][j] = 0
        for row in self.adj_matrix:
            print(row)
    
    def balance(self):
        self.adj_matrix[4][0] = 7
        for i in range(len(self.adj_matrix)):
            for j in range(0,i):
                    self.adj_matrix[j][i] = self.adj_matrix[i][j]

    def print(self):
        print()
        for row in self.adj_matrix:
            print(row)
        print()



G = Graphiest(5)
G.balance()
G.print()

