from graph_environment import Graphiest

# total time complexity O(n!)
# main operation is comparison, checking every graph node as valid positions
# several other operations are addition, and assignments
class hamie:

    has_cycle = None
    list_cycles = []

    def __init__(self):
        self.has_cycle = None

    # checks if a vertex can be added to the path
    # one, if function used to check edge weight from current position to next position
    # another for loop used to compare if the next vertex is repeated in the "path"
    # time complexity = O(n) + O(n) = O(n)
    # main mathematical opeartion: comparison
    def is_safe(self, next_v, graph, path, position):
        # if the weight of the current position in the path to the next vertex is 0 returns
        # false as invalid move
        # time complexity = O(n), looping through path array
        # main operation: comparison
        if graph.get_edge_weight(path[position - 1], next_v) == 0:
            return False

        # checks to see if the next move has already been in the path making it an invalid move
        # time complexity = O(n), looping through path array
        # main operation: comparison
        for i in range(len(path)):
            if path[i] == next_v:
                return False

        # returns true when both above conditions are false, meaning the next move is valid to put into the path
        return True

    # main function of the class that has data structures and calls find_circuit
    def has_hamiltonian(self, graph, Start_v):
        self.has_cycle = False
        # list to keep track of visited vertices
        visited = [False] * graph.vertices_count
        # resulting path that will come out as possible circuits
        path = []
        # initial value is the start vertex
        path.append(Start_v)
        visited[0] = True

        # call find_circuit
        self.find_circuit(graph, 1, path, visited)
        print(len(self.list_cycles))

        # Reduce total amount of "paths" in half due to redundancy. not complete
        # for index in range(0, int(len(self.list_cycles)/2)):
        # self.list_cycles.pop()

        return self.has_cycle

    # recrusive function to find all hamiltonian cycles
    # time complexity = O(n!)
    # main operation: comparison
    def find_circuit(self, graph, position, path, visited):
        # once the path is same length as the graph length, and if there is an
        # edge from the last vertex to the initial vertex
        # add final vertex which is the start vertex
        # time complexity = O(n), loop through the path array
        # main operation: addition
        if len(path) == graph.vertices_count:
            if graph.get_edge_weight(path[len(path) - 1], path[0]) != 0:
                path.append(path[0])

                # once the final start node is re-added at the end, print the entire path
                total_weight = 0
                if len(path) <= 1:
                    return total_weight
                for i in range(1, len(path)):
                    total_weight += graph.get_edge_weight(path[i - 1], path[i])
                self.list_cycles.append([path.copy(), total_weight, total_weight/(len(path)-1)])
                path.pop(len(path) - 1)
                self.has_cycle = True

        # other vertices where the path is not the same length as the graph length
        # time complexity = O(n!)
        # nested loop inside of recusive function
        # main operation is assignment for outer loop
        # main operation for inner loop is comparison
        # for loop going through graph vertices count, with inner nested loop: is_safe
        # that is looping through path array
        for v in range(graph.vertices_count):
            if self.is_safe(v, graph, path, position) and not visited[v]:
                path.append(v)
                visited[v] = True
                # recursion + 1 position
                self.find_circuit(graph, position + 1, path, visited)
                visited[v] = False
                path.pop(len(path) - 1)
