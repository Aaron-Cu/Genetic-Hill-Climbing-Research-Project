from graph_environment import Graphiest
import exhaustive_search
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

print("possible moves")
print(h.possible_moves)

print("Next Move")
print(h.next_move())

print()
print("DFS printout")
