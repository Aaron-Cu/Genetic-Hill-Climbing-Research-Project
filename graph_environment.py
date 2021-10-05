#An application for creating Undirected Fully Connected Weighted Graphs of any size
#


class Graphiest:
    verticies = None
    adj_matrix = None

    def __init__(self, vert):
        verticies = vert
        adj_matrix = [[1 for i in range(verticies)] for j in range(verticies)]
        #print(adj_matrix)
        for row in adj_matrix:
            print(row)

G = Graphiest(5)


