
from graph_environment import Graphiest
from hill_climber import hill_climber
import random
import math

class geneticHillClimber :
    POPULATION_SIZE = None
    STEP_SIZE = None
    GRAPH = None
    POPULATION = None
    AGED = []
    REPLACEMENT_RATE = 0.2
    PARENTCOUNT = None

    # Constructor, initializes graph, population and class variables
    # O(n)
    def __init__(self, graph, popSize, stepSize) :
        self.POPULATION_SIZE = popSize
        self.STEP_SIZE = stepSize
        self.GRAPH = graph
        self.PARENTCOUNT = math.floor(self.POPULATION_SIZE * 0.25)
        self.generateFirstPop()
    
    # Retuns a random Node index from self.GRAPH
    # O(n)
    def randomStart(self):
        return random.randint(0, self.GRAPH.vertices_count - 1)

    # Initializes the population with hill climbers at random starting
    # positions on the graph.
    # O(n)
    def generateFirstPop (self) :
        self.POPULATION = [hill_climber( self.randomStart(), self.GRAPH) for i in range(self.POPULATION_SIZE)]
    
    # Prints each individual's goal status, path, and current fitness
    # O(n)
    def printPopulation(self) :
        if self.POPULATION == None:
            print("No Population")
        else :
            temp = ""
            for index in range(len(self.POPULATION)):
                temp += "\nIndividual: "+ str(index) + "\n\tGoal: "+ str(self.POPULATION[index].is_goal()) + "\n\tPath: " + str(self.POPULATION[index].path) + "\n\tFitness: " + str(self.POPULATION[index].fitness_function())
            print(temp)

    # Prints out the data for each individual moved into the aged solution list
    # O(n)
    def printAged(self) :
        if self.AGED == None:
            print("No Aged Population")
        else :
            temp = ""
            for index in range(len(self.AGED)):
                temp += "\nIndividual "+ str(index) + " Path: " + str(self.AGED[index].path) + " Fitness: " + str(self.AGED[index].fitness_function())
            print(temp)

    # Steps each individual in the population the specified amount.
    # O(n^3)
    def stepPopulaion(self):
        for index in range(len(self.POPULATION)):
            self.POPULATION[index].step(self.STEP_SIZE) # O(n^2)

    # Partioning for quicksort
    # 0(logn)
    def partitionAged(self, low, high):
        i = (low-1)
        pivot = self.AGED[high].fitness_function()

        for j in range(low, high):
            if self.AGED[j].fitness_function() <= pivot:
                i= i+1
                self.AGED[i], self.AGED[j] = self.AGED[j], self.AGED[i]

        self.AGED[i+1], self.AGED[high] = self.AGED[high], self.AGED[i+1]
        return (i+1)
    
    # Quicksort of Aged
    # O(logn)
    def sortAged(self, low, high):
        if len(self.AGED) <= 1:
            return
        if low < high:
            pi = self.partitionAged(low, high)

            self.sortAged(low, pi-1)
            self.sortAged(pi+1, high)

    # Partioning for quicksort
    # 0(logn)
    def partitionPopulation(self, low, high):
        i = (low-1)
        pivot = self.POPULATION[high].fitness_function()

        for j in range(low, high):
            if self.POPULATION[j].fitness_function() <= pivot:
                i= i+1
                self.POPULATION[i], self.POPULATION[j] = self.POPULATION[j], self.POPULATION[i]

        self.POPULATION[i+1], self.POPULATION[high] = self.POPULATION[high], self.POPULATION[i+1]
        return (i+1)
    
    # Returns true if solution is already found in Aged
    # O(n)
    def existsInAged(self, index):
        path = self.POPULATION[index].path
        for i in range(len(self.AGED)):
            if path == self.AGED[i].path:
                return True
        return False
    
    # Quicksort of Population
    # O(logn)
    def sortPopulation(self, low, high):
        if len(self.POPULATION) <= 1:
            return
        if low < high:
            pi = self.partitionPopulation(low, high)

            self.sortPopulation(low, pi-1)
            self.sortPopulation(pi+1, high)

    # Finds the parents for the next generation and Ages them out of 
    # the population, the next generation is then created based on the
    # fittest individuals in aged
    # O(n^2)
    def findParents(self):
        self.sortPopulation(0, self.POPULATION_SIZE-1)
        for i in range(len(self.POPULATION)):
            if self.POPULATION[i].is_goal() and self.existsInAged(i) == False: # O(n)
                self.AGED.append(self.POPULATION[i])
        self.sortAged(0, len(self.AGED)-1)
        print()
        print(len(self.AGED))
        print(len(self.POPULATION))
        print()
        counter = 0
        parentNum = 0
        while counter <= self.POPULATION_SIZE-1:
            print(counter)
            print(parentNum)
            print()
            if len(self.AGED) > 0:
                self.POPULATION[counter] = hill_climber(self.AGED[parentNum].path[random.randint(0,2)], self.GRAPH)
            else:
                self.POPULATION[counter] = hill_climber( self.randomStart(), self.GRAPH)
            counter = counter + 1
            parentNum = parentNum + 1
            if parentNum >= len(self.AGED) or parentNum >= self.PARENTCOUNT:
                parentNum = 0

    # Random chance of adding new random starting individuals to the
    # population.
    # O(n)
    def addMutations(self):
        for i in range(len(self.POPULATION)):
            if (random.randint(1,100) <= 5):
                print("MUTATION")
                self.POPULATION[i] = hill_climber( self.randomStart(), self.GRAPH)
    
    # returns the fittest individual from aged as solution
    # O(logn) (quicksort required)
    def printBestSolution(self):
        print("\nIndividual "+ str(0) + " Path: " + str(self.AGED[0].path) + " Fitness: " 
            + str(self.AGED[0].fitness_function()) +" Nodes: " + str(len(self.AGED[0].path)-1) +
            " Length of Path: " + str(self.AGED[0].getPathWeight()))

    # Runs the genetic algorithm for the specified number of generations
    # O(n^3)
    def run(self, generations):
        for i in range(generations):
            self.stepPopulaion()
            self.printPopulation()
            self.findParents()
            self.printPopulation()
            self.addMutations()
            self.printPopulation



