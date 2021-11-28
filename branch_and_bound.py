import math
from graph_environment import Graphiest

class branchAndBound:
    graph = None
    adj = None
    N = None
    maxsize = None
    final_path = None
    visited = None
    final_res = None

    def __init__(self, graph):
        self.graph = graph
        self.adj = graph.adj_matrix
        self.N = graph.vertices_count
        self.final_path = [None] * (self.N + 1)
        self.visited = [False] * self.N
        self.maxsize = float('inf')
        self.final_res = self.maxsize
        self.TSP()
        print()
        print("minimum cost :", self.final_res)
        print("path taken: ", end=' ')
        for i in range(self.N + 1):
            print(self.final_path[i], end=' ')
        sum = 0
        for i in range(1,self.N + 1):
            sum = sum + self.graph.get_edge_weight(self.final_path[i-1],self.final_path[i])
        print("Fitness: "+str(sum/self.N))
        print()

    def copyToFinal(self, current_path):
        self.final_path[:self.N + 1] = current_path[:]
        self.final_path[self.N] = current_path[0]


    def firstMin(self, i):
        min = self.maxsize
        for k in range(self.N):
            if self.adj[i][k] < min and i != k:
                min = self.adj[i][k]
        return min


    def secondMin(self, i):
        first, second = self.maxsize, self.maxsize
        for j in range(self.N):
            if i == j:
                continue
            if self.adj[i][j] <= first:
                second = first
                first = self.adj[i][j]
            elif(self.adj[i][j] <= second and self.adj[i][j] != first):
                second = self.adj[i][j]
        return second


    def TSPRec(self, current_bound, current_weight, level, current_path,):
        self.final_res
        if level == self.N:
            if self.adj[current_path[level - 1]][current_path[0]] != 0:
                current_res = current_weight + \
                    self.adj[current_path[level - 1]][current_path[0]]
                if current_res < self.final_res:
                    self.copyToFinal(current_path)
                    final_res = current_res
            return
        for i in range(self.N):
            if (self.adj[current_path[level - 1]][i] != 0 and self.visited[i] == False):
                temp = current_bound
                current_weight += self.adj[current_path[level - 1]][i]
                if level == 1:
                    current_bound -= ((self.firstMin(
                                    current_path[level - 1]) + self.firstMin(i)) / 2)
                else:
                    current_bound -= ((self.secondMin(
                                    current_path[level - 1]) + self.firstMin(i)) / 2)
                if current_bound + current_weight < self.final_res:
                    current_path[level] = i
                    self.visited[i] = True
                    self.TSPRec(current_bound, current_weight,
                        level + 1, current_path)
                current_weight -= self.adj[current_path[level - 1]][i]
                current_bound = temp
                self.visited = [False] * len(self.visited)
                for j in range(level):
                    if current_path[j] != -1:
                        self.visited[current_path[j]] = True


    def TSP(self):
        current_bound = 0
        current_path = [-1] * (self.N + 1)
        self.visited = [False] * self.N
        for i in range(self.N):
            current_bound += (self.firstMin(i) + self.secondMin(i))
        current_bound = math.ceil(current_bound / 2)
        self.visited[0] = True
        current_path[0] = 0
        self.TSPRec(current_bound, 0, 1, current_path,)


