from graph_environment import Graphiest


class hamie:

    has_cycle = None
    list_cycles = []

    def __init__(self):
        self.has_cycle = None

    # checks if a vertex can be added to the path
    # time complexity = O(n) + O(n) = O(n)
    # one if function where ch;ecking position of the amount of edges there are inputed. with another for loop
    # that goes through the array/list of path, to compare if the next vertex is repeated
    # main mathematical "work" is comparison
    def is_safe(self, next_v, graph, path, position):
        # if the weight of the current position in the path to the next vertex is 0 returns false as not possible move
        if graph.get_edge_weight(path[position - 1], next_v) == 0:
            return False

        # checks to see if the next move has already been in the path making it an invalid move
        for i in range(len(path)):
            if path[i] == next_v:
                return False

        # returns true when both above conditions are false, meaning the next move is valid to put into the path
        return True

    def has_hamiltonian(self, graph, Start_v):
        self.has_cycle = False
        # list to keep track of visited vertices
        visited = [False] * graph.vertices_count
        # resulting path that will come out as possible circuits
        path = []
        # initial value is the start vertex
        path.append(Start_v)
        visited[0] = True

        # call find hamiltonian circuit
        self.find_circuit(graph, 1, path, visited)
        print(len(self.list_cycles))

        # for index in range(0, int(len(self.list_cycles)/2)):
        # self.list_cycles.pop()

        return self.has_cycle

    #
    #
    def find_circuit(self, graph, position, path, visited):
        # once the path is same length as the graph lenght, and if there is an edge from the last vertex to the
        # initial vertex, add final vertex which is the start vertex
        #               print("the lengeth of the path is " + str(len(path)) + " the vert count is " + str(graph.vertices_count) +" and the cirrent path is ")
        #               print(*path, sep = ", ")
        #
        if len(path) == graph.vertices_count:
            #           print("here")
            # this part is O(n). the main task is addition. once the path is full, it will add up all weights of the path
            if graph.get_edge_weight(path[len(path) - 1], path[0]) != 0:
                path.append(path[0])
                # once the final start node is re-added at the end, print the entire path
                # print(*path, sep = ", ")
                total_weight = 0
                if len(path) <= 1:
                    return total_weight
                for i in range(1, len(path)):
                    total_weight += graph.get_edge_weight(path[i - 1], path[i])
                self.list_cycles.append([path.copy(), total_weight])
                path.pop(len(path) - 1)
                self.has_cycle = True

        # other vertices where the path is not the same length as the graph length
        # O(n!) going through a for loop of the number of vertices count. where that for loop, loops though another
        # for loop. essentially a nested for loop, inside of recursive function. as the graph gets larger, multiplied
        # by n size
        for v in range(graph.vertices_count):
            #                       print(str(position) +" to " +str(v))
            if self.is_safe(v, graph, path, position) and not visited[v]:
                path.append(v)
                visited[v] = True
                self.find_circuit(graph, position + 1, path, visited)
                visited[v] = False
                path.pop(len(path) - 1)
