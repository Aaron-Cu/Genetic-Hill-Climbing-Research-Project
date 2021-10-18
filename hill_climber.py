from graph_environment import Graphiest
import exhaustive_search

# a class for a hill-climber object to be implemented
# by a genetic algorithm.
class hill_climber:
    
    path = None
    current =  None
    possible_moves = None
    graph = None

    # initializes the hill climber to a given start posion on 
    # 'graph'
    # complexity of O(n) (because of get_neighbors function)
    def __init__(self, start, graph):
        self.current = start
        self.graph = graph
        self.path = []
        self.path.append(self.current)
        self.get_moves()
    
    # Sets the list of possible moves to the neighbors of a give 
    # current position
    # Complexity of O(n)
    def get_moves(self):
        self.possible_moves = self.graph.get_neighbors(self.current)
        temp = []
        for index in range(0, len(self.possible_moves)):
            if self.possible_moves[index] not in self.path:
                temp.append(self.possible_moves[index])
        self.possible_moves = temp
    
    # Advances through a set number of state speces
    # Complexity of O(n^2)
    def step(self, step_size):
        for i in range(step_size):
            if self.is_goal() == False:
                if self.has_next_move():
                    # O(n) + O(1)
                    self.take_move(self.next_move())

    # Returns True if there are moves that can be made
    # Complexity of O(1)
    def has_next_move(self):
        if len(self.possible_moves) == 0:
            return False
        return True
    
    # Updates the array of availible moves to current position
    # Complexity of O(n)
    def next_move(self):
        self.get_moves
        if self.has_next_move() == False:
            return -1
        min = 0
        for index in range(0, len(self.possible_moves)):
            if self.graph.get_edge_weight(self.current, self.possible_moves[index]) < self.graph.get_edge_weight(self.current, self.possible_moves[min]):
                min = index
        return self.possible_moves[min]
    
    # Changes current to a new positon and adds the new move to the
    # current path taken.
    # Complexity of O(1)
    def take_move(self, move):
        if move in self.possible_moves:
            self.current = move
            self.path.append(self.current)
            self.get_moves()
    
    # Returns a fitness variable for exaluation
    # Complexity of O(n)
    def fitness_function(self):
        total_weight = 0
        if len(self.path) <= 1:
            return total_weight
        for i in range(1, len(self.path)):
            total_weight += self.graph.get_edge_weight(self.path[i-1], self.path[i])
        if self.is_goal:
            total_weight += self.graph.get_edge_weight(self.path[0], self.path[len(self.path)-1])
        return total_weight

    # Returns true if there are no more possible moves
    # Complexity of O(1)
    def is_dead_end(self):
        if self.graph.vertices_count == len(self.path):
            return True
        return False

    # Returns true if the current state is a goal state
    # Complexity of O(1)
    def is_goal(self):
        if self.is_dead_end():
            if self.graph.is_edge(self.path[len(self.path)-1], self.path[0]):
                return True
        return False

    