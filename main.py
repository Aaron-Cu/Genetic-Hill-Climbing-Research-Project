from graph_environment import Graphiest
import exhaustive_search
from has_hamiltonian import hamie
from hill_climber import hill_climber

# Code for testing the Class Functions
# Output in the console will be used to verify functionality
print("Creating a Fully Connected Graph of size 5 and weights bound by 100")
G = Graphiest(5, 100)

# TESTING ADDING WEIGHTS
# print("Adding weights bounded to 100")
# G.add_weights(100)  # 100 upper bound test
# G.print()

# TESTING BALANCING
# print("Setting bottom Left to 7")
# G.adj_matrix[4][0] = 7
# G.print()
# print("Balancing Right..")
# G.balance()
# G.print()

print("Fettching neighbors of vertex 2")
print()
print(G.get_neighbors(2))
print()

print("Getting weigt of edge from vertex 2 to 4")
print()
print(G.get_edge_weight(2,4))
print()

print("Making a Hill CLimber")
h = hill_climber(0, G)

# First Step
print("current position is")
print(h.current)

print("possible moves")
print(h.possible_moves)

print()
print("taking next move")
h.take_move(h.next_move())

print("new current is")
print(h.current)

print("possible moves")
print(h.possible_moves)

print("current path is")
print(h.path)

print("fitness is ")
print(h.fitness_function())

# Second Step
print()
print("current position is")
print(h.current)

print("possible moves")
print(h.possible_moves)

print()
print("taking next move")
h.take_move(h.next_move())

print("new current is")
print(h.current)

print("possible moves")
print(h.possible_moves)

print("current path is")
print(h.path)

print("fitness is ")
print(h.fitness_function())

# Third Step
print()
print("current position is")
print(h.current)

print("possible moves")
print(h.possible_moves)

print()
print("taking next move")
h.take_move(h.next_move())

print("new current is")
print(h.current)

print("possible moves")
print(h.possible_moves)

print("current path is")
print(h.path)

print("fitness is ")
print(h.fitness_function())

# Frouth Step
print()
print("current position is")
print(h.current)

print("possible moves")
print(h.possible_moves)

print()
print("taking next move")
h.take_move(h.next_move())

print("new current is")
print(h.current)

print("possible moves")
print(h.possible_moves)

print("current path is")
print(h.path)

print("fitness is ")
print(h.fitness_function())

print()
print()
print("is goal state")
print(h.is_goal())

print()
print("________________________________")
print()
print("making second hill climber")
h_2 = hill_climber(0, G)

print ("taking four steps on same graph")
h_2.step(4)

print("current is")
print(h.current)

print("possible moves")
print(h_2.possible_moves)

print("current path is")
print(h_2.path)

print("fitness is ")
print(h_2.fitness_function())

print()
print()
print("is goal state")
print(h_2.is_goal())

print()
print("DFS printout")

ham = hamie()
print("has ham")
print(ham.has_hamiltonian(G, 0))
print(*ham.list_cycles, sep = "\n")