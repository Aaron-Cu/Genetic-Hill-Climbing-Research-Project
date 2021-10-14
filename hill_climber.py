from graph_environment import Graphiest
import exhaustive_search

class hill_climber:

    path = None
    current =  None
    possible_moves = None
    graph = None

    def __init__(self, start, graph):
        self.current = start
        self.graph = graph
        self.path = []
        self.get_moves()
    
    def get_moves(self):
        self.possible_moves = self.graph.get_neightbors(self.current)
    
    def step(self, step_size):
        for i in range(step_size):
            if self.is_goal() == False:
                if self.has_next_move():
                    self.take_move(self.next_move())

    def has_next_move(self):
        if len(self.graph.get_neighbors(self.current)) == 0:
            return False
        return True
    
    def next_move(self):
        self.possible_moves = self.graph.get_neighbors(self.current)
        if self.has_next_move() == False:
            return -1
        min = 0
        for index in self.possible_moves:
            if self.graph.get_edge_weight(self.current, self.possible_moves[index]) < self.graph.get_edge_weight(self.current, self.possible_moves[min]):
                min = index
        return min
    
    def take_move(self, move):
        self.path.apend(self.current)
        self.current = move
        self.get_moves()

    def fitness_function(self):
        total_weight = 0
        if len(self.path) == 0:
            return total_weight
        for i in range(1, len(self.path)-1):
            total_weight += self.graph.get_edge_weight(self.path[i-1], self.path[i])
        return total_weight

    def is_dead_end(self):
        return

    def is_goal(self):
        if len(self.path) == self.graph.vertices_count:
            if self.graph.is_edge(self.path[len(self.path)-1], self.path[0]):
                return True
        return False

    