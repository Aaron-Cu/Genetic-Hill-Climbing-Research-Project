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
        # stores final minium weight of the shortest tour
        self.final_res = self.maxsize
        self.TSP()
        print()
        print("minimum cost :", self.final_res)
        print("path taken: ", end=' ')
        for i in range(self.N + 1):
            print(self.final_path[i], end=' ')
        sum = 0
        for i in range(1, self.N + 1):
            sum = sum + \
                self.graph.get_edge_weight(
                    self.final_path[i-1], self.final_path[i])
        print("Fitness: "+str(sum/self.N))
        print()

    # function to copy the current path to the final path
    def copyToFinal(self, current_path):
        self.final_path[:self.N + 1] = current_path[:]
        self.final_path[self.N] = current_path[0]

    # finds first minimum edge cost with end at vertex 1
    def firstMin(self, i):
        min = self.maxsize
        for k in range(self.N):
            if self.adj[i][k] < min and i != k:
                min = self.adj[i][k]
        return min

    # finds second minimum edge cost with end at vertex 1
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

    # current bound is the lower bound of the root
    # current weight is the weight of the path so far
    # level is the current level while moving in the space search tree
    def TSPRec(self, current_bound, current_weight, level, current_path,):
        self.final_res
        # base case where all nodes have been covered once
        if level == self.N:
            # checks if t here is a path back to the start
            if self.adj[current_path[level - 1]][current_path[0]] != 0:
                current_res = current_weight + \
                    self.adj[current_path[level - 1]][current_path[0]]
                # current_res is the total weight so far
                if current_res < self.final_res:
                    self.copyToFinal(current_path)
                    final_res = current_res
            return
        # for other levels, nodes not all reached, iterate through al lvertices to build seach space tree recursively
        for i in range(self.N):
            # checks to see if the next vertix is not the same or not visited already
            if (self.adj[current_path[level - 1]][i] != 0 and self.visited[i] == False):
                temp = current_bound
                current_weight += self.adj[current_path[level - 1]][i]
                # level 1 calculations
                if level == 1:
                    current_bound -= ((self.firstMin(
                        current_path[level - 1]) + self.firstMin(i)) / 2)
                # for level 2 and above
                else:
                    current_bound -= ((self.secondMin(
                        current_path[level - 1]) + self.firstMin(i)) / 2)
                # current_bound and current_weight is the lower bound for node arrived
                # if the lower bound is less than the final result, further nodes need exploration
                if current_bound + current_weight < self.final_res:
                    current_path[level] = i
                    self.visited[i] = True
                    # recursively call TSP for next level
                    self.TSPRec(current_bound, current_weight,
                                level + 1, current_path)
                # else reset the lower bound
                current_weight -= self.adj[current_path[level - 1]][i]
                current_bound = temp
                # also reset the visited array
                self.visited = [False] * len(self.visited)
                for j in range(level):
                    if current_path[j] != -1:
                        self.visited[current_path[j]] = True

    # calculates lower bound for the root node for all edges
    def TSP(self):
        current_bound = 0
        current_path = [-1] * (self.N + 1)
        self.visited = [False] * self.N
        # calculate initial bound
        for i in range(self.N):
            current_bound += (self.firstMin(i) + self.secondMin(i))
        # rounds current bound to lowest integer
        current_bound = math.ceil(current_bound / 2)
        # always start at vertex 0
        self.visited[0] = True
        current_path[0] = 0
        # calls TSPrec for the current weight equal to 0 and 1
        self.TSPRec(current_bound, 0, 1, current_path,)
