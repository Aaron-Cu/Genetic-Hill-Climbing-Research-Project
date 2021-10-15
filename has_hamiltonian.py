from graph_environment import Graphiest

# checks if a vertex can be added to the path
def is_safe(next_v, graph, path, position):
    # if the weight of the current position in the path to the next vertex is 0 returns false as not possible move
    if graph.get_edge_weight(path[position - 1], next_v) == 0:
        return False

    # checks to see if the next move has already been in the path making it an invalid move
    for i in range(position):
        if path[i] == next_v:
            return False

    # returns true when both above conditions are false, meaning the next move is valid to put into the path
    return True


has_cycle = None


def has_hamiltonian(graph, Start_v):
    has_cycle == False
    # list to keep track of visited vertices
    visited = [False] * graph.vertices_count
    # resulting path that will come out as possible circuits
    path = []
    # initial value is the start vertex
    path.append(Start_v)
    visited[0] = True

    # call find hamiltonian circuit
    find_circuit(graph, 1, path, visited)
    if has_cycle == False:
        print("no circuit")


def find_circuit(graph, position, path, visited):
    # once the path is same length as the graph lenght, and if there is an edge from the last vertex to the
    # initial vertex, add final vertex which is the start vertex
    if position == graph.vertices_count:
        if graph.get_edge_weight(path[len(path) - 1], path[0]) != 0:
            path.append(path[0])
            # once the final start node is re-added at the end, print the entire path
            for i in path:
                print(path[i], end=" ")
            print(" ")
            path.pop(len(path) - 1)
            has_cycle == True
    # other vertices where the path is not the same length as the graph length
    for v in range(graph.vertices_count):
        if is_safe(v, graph, path, position) and not visited[v]:
            path.append(v)
            visited[v] = True
            find_circuit(graph, position + 1, path, visited)
            visited[v] = False
            path.pop(len(path) - 1)
