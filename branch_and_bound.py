import math
from graph_environment import Graphiest

adj = Graphiest.adj_matrix
N = Graphiest.vertices_count
maxsize = None
maxsize = float('inf')


def copyToFinal(current_path):
    final_path[:N + 1] = current_path[:]
    final_path[N] = current_path[0]


def firstMin(adj, i):
    min = maxsize
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]
    return min


def secondMin(adj, i):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]
        elif(adj[i][j] <= second and adj[i][j] != first):
            second = adj[i][j]
    return second


def TSPRec(adj, current_bound, current_weight, level, current_path, visited):
    global final_res
    if level == N:
        if adj[current_path[level - 1]][current_path[0]] != 0:
            current_res = current_weight + \
                adj[current_path[level - 1]][current_path[0]]
            if current_res < final_res:
                copyToFinal(current_path)
                final_res = current_res
        return
    for i in range(N):
        if (adj[current_path[level - 1]][i] != 0 and visited[i] == False):
            temp = current_bound
            current_weight += adj[current_path[level - 1]][i]
            if level == 1:
                current_bound -= ((firstMin(adj,
                                  current_path[level - 1]) + firstMin(adj, i)) / 2)
            else:
                current_bound -= ((secondMin(adj,
                                  current_path[level - 1]) + firstMin(adj, i)) / 2)
            if current_bound + current_weight < final_res:
                current_path[level] = i
                visited[i] = True
                TSPRec(adj, current_bound, current_weight,
                       level + 1, current_path, visited)
            current_weight -= adj[current_path[level - 1]][i]
            current_bound = temp
            visited = [False] * len(visited)
            for j in range(level):
                if current_path[j] != -1:
                    visited[current_path[j]] = True


def TSP(adj):
    current_bound = 0
    current_path = [-1] * (N + 1)
    visited = [False] * N
    for i in range(N):
        current_bound += (firstMin(adj, i) + secondMin(adj, i))
    current_bound = math.ceil(current_bound / 2)
    visited[0] = True
    current_path[0] = 0
    TSPRec(adj, current_bound, 0, 1, current_path, visited)


final_path = [None] * (N + 1)
visited = [False] * N
final_res = maxsize
TSP(adj)
print("minimum cost :", final_res)
print("path taken: ", end=' ')
for i in range(N + 1):
    print(final_path[i], end=' ')
