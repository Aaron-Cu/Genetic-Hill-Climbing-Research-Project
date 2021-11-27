from graph_environment import Graphiest
import exhaustive_search
from has_hamiltonian import hamie
from hill_climber import hill_climber
from geneticHillClimber import geneticHillClimber


# Code for testing the Class Functions
# Output in the console will be used to verify functionality
print("\n")
print("Creating a Fully Connected Graph of size 5 and weights bound by 100")
G = Graphiest(5, 100)


# Test Graph
def test_graph():
    print("\n")
    print("Fettching neighbors of vertex 2")
    print()
    print(G.get_neighbors(2))
    print()

    print("Getting weigt of edge from vertex 2 to 4")
    print()
    print(G.get_edge_weight(2,4))
    print()
    print("\n")

def test_hill():
    print("\n")
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

    print()
    print("is goal state")
    print(h_2.is_goal())
    print("\n")

    print("current path is")
    print(h_2.path)

    print("fitness is ")
    print(h_2.fitness_function())

def test_has_ham():
    print("\n")
    ham = hamie()
    print("has ham")
    print(ham.has_hamiltonian(G, 0))
    print(*ham.list_cycles, sep = "\n")
    print("\n")

def test_genetic_hill_climber() :
    geneticTest = geneticHillClimber(G, 4 , 2)
    print("\nGraph:")
    geneticTest.GRAPH.print()
    print("\nPopulation size: ") 
    print(geneticTest.POPULATION_SIZE)
    print("\nStep size: ")
    print(geneticTest.STEP_SIZE)
    print("\nPopulation: ")
    geneticTest.printPopulation()
    print("\nAged: ")
    geneticTest.printAged()

    print("\n_________________________________________\n")
    print("TAKING A POPULATION STEP OF SIZE "+str(geneticTest.STEP_SIZE)+".")
    geneticTest.stepPopulaion()
    print("\n_________________________________________\n")

    print("\nPopulation size: ") 
    print(geneticTest.POPULATION_SIZE)
    print("\nStep size: ")
    print(geneticTest.STEP_SIZE)
    print("\nPopulation: ")
    geneticTest.printPopulation()
    print("\nAged: ")
    geneticTest.printAged()

    print("\n_________________________________________\n")
    print("TAKING A POPULATION STEP OF SIZE "+str(geneticTest.STEP_SIZE)+".")
    geneticTest.stepPopulaion()
    print("\n_________________________________________\n")

    print("\nPopulation size: ") 
    print(geneticTest.POPULATION_SIZE)
    print("\nStep size: ")
    print(geneticTest.STEP_SIZE)
    print("\nPopulation: ")
    geneticTest.printPopulation()
    print("\nAged: ")
    geneticTest.printAged()

    print("\n_________________________________________\n")
    print("TAKING A POPULATION STEP OF SIZE "+str(geneticTest.STEP_SIZE)+".")
    geneticTest.stepPopulaion()
    print("\n_________________________________________\n")

    print("\nPopulation size: ") 
    print(geneticTest.POPULATION_SIZE)
    print("\nStep size: ")
    print(geneticTest.STEP_SIZE)
    print("\nPopulation: ")
    geneticTest.printPopulation()
    print("\nAged: ")
    geneticTest.printAged()

    print("\n_________________________________________\n")
    print("SORTING POPULATION.")
    geneticTest.sortPopulation(0, geneticTest.POPULATION_SIZE-1)
    print("\n_________________________________________\n")
    geneticTest.printPopulation()


    

end = False

def _end():
    global end
    end = True

# mapped the inputs to the function blocks
options = {'end' : _end,
             '0' : test_graph,
             '1' : test_hill,
             '2' : test_has_ham,
             '3' : test_genetic_hill_climber,
}

while(end == False):
    
    options[input(
        "=========================================\n"+
        "Enter...\n" +
        " 0  : To test the Graph.\n"+
        " 1  : To test the Hill Climber.\n"+
        " 2  : To test the Exhustive Search.\n"+
        " 3  : To test the Genetic Hill Climber.\n"+
        "end : To end this program.\n"+
        "=========================================\n\n"
    )]()
