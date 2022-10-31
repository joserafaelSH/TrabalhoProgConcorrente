from typing import List
import math
import random

class InputFile:
    def __init__(self, fileName):
        self.fileName = fileName
        self.cityPoints = []
        self.inputSize = 0

    def lerEntrada(self)->None:
        c = 0 
        with open(self.fileName) as file:
            for line in file:
                if c<6:
                    c+=1
                    continue

                line = line.strip() 
                aux = line.split(" ")
                if aux[0] == "EOF":
                    break
                aux = list(map(float, aux))
                self.cityPoints.append(aux[1:]) 

        self.inputSize = len(self.cityPoints)

    def get_city_points(self):
        return self.cityPoints

    def get_input_size(self):
        return self.inputSize

class Genetic:
    def __init__(self, mutationRate:float, nGenerations:int, popSize: int, inputSize: int, cityPoints:List[List[float]], outputFile:str, op:int, t:int) -> None:
        self.mutationRate = mutationRate
        self.nGenerations = nGenerations
        self.popSize = popSize
        self.inputSize = inputSize
        self.bestSolution = 0
        self.population = []
        self.fitness = []
        self.cityPoints = cityPoints
        self.result = []
        self.outputFile = outputFile
        self.op = op
        self.t = t


    def pitagoras(self, x1:float, y1: float, x2: float, y2: float) -> float:
        x = x2-x1
        y = y2-y1
        raiz = (x*x) + (y*y)
        return math.sqrt(raiz)

    def getIndex(self, v:List[int], K:int) -> int:
        idx = v.index(K)
        return idx
  

    def findLowestFit(self) -> int:
        idx = 0
        val = self.fitness[0]
        for i in range(0, self.popSize):
            if val < self.fitness[i]:
                val = self.fitness[i]
                idx = idx

        return idx

    def findBestFit(self) -> int:
        idx = 0
        val = self.fitness[0]
        for i in range(0, self.popSize):
            if val < self.fitness[i]:
                val = self.fitness[i]
                idx = idx

        return idx

    def findElem(self, v:List[int], k:int) -> bool:
        return True if k in v else False

    def createInitialPopulation(self) -> None:
        for _ in range(self.popSize):
            populacao = [i for i in range(self.inputSize)]
            random.shuffle(populacao) 
            self.population.append(populacao)
    
    def get_population(self):
        return self.population

    def get_fitness(self):
        return self.fitness
    
    def pathValue(self, path:List[int])->float: 
        total = 0
        for i in range(0, len(path)-1):
            total += self.pitagoras(self.cityPoints[path[i]][0], self.cityPoints[path[i]][1],
            self.cityPoints[path[i+1]][0], self.cityPoints[path[i+1]][1])

        return total

    def calcularFitness(self, population: List[List[int]]):
        for pop in population:
            self.fitness.append(1.0/self.pathValue(pop))
    
    def showPath(self, path: List[int]):
        for c in path:
            print(c)
        print()

    def rouletteSelection(self):
        total = sum(self.fitness)
        probability = []
        
        for fit in self.fitness:
            probability.append(fit/total)

        offset = 0.0
        pick = 0
        c = 0
        rng = random.random()

        while c < self.popSize:
            offset+=probability[c]
            if rng < offset:
                return c 
            c+=1
        return pick

    def mutation(self, path: List[int]):
        pos1 = random.randint(0, self.inputSize-1)
        pos2 = random.randint(0, self.inputSize-1)

        path[pos1], path[pos2] = path[pos2], path[pos1]

    def oX(self, ind1, ind2):
        size = min(len(ind1), len(ind2))
        a, b = random.sample(range(size), 2)
        if a > b:
            a, b = b, a

        holes1, holes2 = [True] * size, [True] * size
        for i in range(size):
            if i < a or i > b:
                holes1[ind2[i]] = False
                holes2[ind1[i]] = False

        temp1, temp2 = ind1, ind2
        k1, k2 = b + 1, b + 1
        for i in range(size):
            if not holes1[temp1[(i + b + 1) % size]]:
                ind1[k1 % size] = temp1[(i + b + 1) % size]
                k1 += 1

            if not holes2[temp2[(i + b + 1) % size]]:
                ind2[k2 % size] = temp2[(i + b + 1) % size]
                k2 += 1

        # Swap the content between a and b (included)
        for i in range(a, b + 1):
            ind1[i], ind2[i] = ind2[i], ind1[i]

        if self.pathValue(ind1) < self.pathValue(ind2):
            self.result = ind1
        else:
            self.result = ind2

    def cX(self, ind1, ind2):
        size = min(len(ind1), len(ind2))
        cxpoint1 = random.randint(1, size)
        cxpoint2 = random.randint(1, size - 1)
        if cxpoint2 >= cxpoint1:
            cxpoint2 += 1
        else: 
            cxpoint1, cxpoint2 = cxpoint2, cxpoint1

        ind1[cxpoint1:cxpoint2], ind2[cxpoint1:cxpoint2] \
            = ind2[cxpoint1:cxpoint2], ind1[cxpoint1:cxpoint2]

        if self.pathValue(ind1) < self.pathValue(ind2):
            self.result = ind1
        else:
            self.result = ind2

    def populationMaintenance(self):
        idx = self.findLowestFit()

        if self.pathValue(self.result) < self.pathValue(self.population[idx]):
            self.population[idx] = self.result

    def run(self):
        out = open(self.outputFile, 'w')

        gen = 0
        self.createInitialPopulation()
        self.calcularFitness(self.population)

        while gen < self.nGenerations:
            pathIdx1 = self.rouletteSelection()
            pathIdx2 = self.rouletteSelection()

            if self.op == 1:
                self.oX(self.population[pathIdx1], self.population[pathIdx2])
            else:
                self.cX(self.population[pathIdx1], self.population[pathIdx2])

            mut = random.random()

            if mut <= self.mutationRate: 
                self.mutation(self.result)
            
            self.populationMaintenance()
            best = self.findBestFit()

            out.write(str(self.pathValue(self.population[best])) + '\n')

            gen+=1

    