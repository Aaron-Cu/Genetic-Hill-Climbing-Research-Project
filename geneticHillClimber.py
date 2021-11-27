
from graph_environment import Graphiest
from hill_climber import hill_climber
import random

class geneticHillClimber :
    POPULATION_SIZE = None
    STEP_SIZE = None
    GRAPH = None
    POPULATION = None
    AGED = None
    REPLACEMENT_RATE = 0.2

    def __init__(self, graph, popSize, stepSize) :
        self.POPULATION_SIZE = popSize
        self.STEP_SIZE = stepSize
        self.GRAPH = graph

        self.generateFirstPop()
    
    # O(n)
    def randomStart(self):
        return random.randint(0, self.GRAPH.vertices_count - 1)

    # O(n)
    def generateFirstPop (self) :
        self.POPULATION = [hill_climber( self.randomStart(), self.GRAPH) for i in range(self.POPULATION_SIZE)]
    
    # O(n)
    def printPopulation(self) :
        if self.POPULATION == None:
            print("No Population")
        else :
            temp = ""
            for index in range(len(self.POPULATION)):
                temp += "\nIndividual: "+ str(index) + "\n\tGoal: "+ str(self.POPULATION[index].is_goal()) + "\n\tPath: " + str(self.POPULATION[index].path) + "\n\tFitness: " + str(self.POPULATION[index].fitness_function())
            print(temp)

    def printAged(self) :
        if self.AGED == None:
            print("No Aged Population")
        else :
            temp = ""
            for index in range(len(self.AGED)):
                temp += "\nIndividual "+ str(index) + " Path: " + str(self.AGED[index].path) + " Fitness: " + str(self.AGED[index].fitness_function())
            print(temp)

    def stepPopulaion(self):
        for index in range(len(self.POPULATION)):
            self.POPULATION[index].step(self.STEP_SIZE)

    def sortPopulation(self):
        pass

    def findParents(self):
        parentOne = none
        parentTwo = none
        pass


    def newCimberFromCrossover(self) :
        pass


