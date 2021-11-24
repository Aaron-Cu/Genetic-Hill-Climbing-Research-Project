
from graph_environment import Graphiest
from hill_climber import hill_climber
import random

class geneticHillClimber :
    POPULATION_SIZE = None
    STEP_SIZE = None
    GRAPH = None
    POPULATION = None
    AGED = None

    def __init__(self, graph, popSize, stepSize) :
        self.POPULATION_SIZE = popSize
        self.STEP_SIZE = stepSize
        self.GRAPH = graph

        self.generateFirstPop()
    
    def randomStart(self):
        return random.randint(0, self.GRAPH.vertices_count - 1)

    def generateFirstPop (self) :
        self.POPULATION = [hill_climber( self.randomStart(), self.GRAPH) for i in range(self.POPULATION_SIZE)]
    
    def printPopulation(self) :
        temp = ""
        for index in range(len(self.POPULATION)):
            temp += "\nIndividual "+ str(index) + " Path: " + str(self.POPULATION[index].path) + " Fitness: " + str(self.POPULATION[index].fitness_function())
        print(temp)

    def printAged(self) :
        pass

    def findParents(self):
        pass

    def newCimberFromCrossover(self) :
        pass


