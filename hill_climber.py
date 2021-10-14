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
    
    def step(self, step_size):
        for i in range(step_size):
            if self.is_goal() == False:
                self.take_move(self.next_move())
    
    def next_move(self):
        self.possible_moves = self.graph.get_neighbors(self.current)
        min = self.graph.get_edge_weight(self.current , self.possible_moves[0])
        for index in self.possible_moves:
            return
    
    def take_move(self):
        return

    def fitness_function(self):
        return

    def is_goal(self):
        return

    