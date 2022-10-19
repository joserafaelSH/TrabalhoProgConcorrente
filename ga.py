import random
import math
from typing import List

class Ga:

    def __init__(self, tamanhoPopulacao:int, taxaMutacao:float, numeroGeracoes:int, arqEntrada:str) -> None:
        self.tamanhoPopulacao = tamanhoPopulacao
        self.taxaMutacao = taxaMutacao 
        self.numeroGeracoes = numeroGeracoes 
        self.arqEntrada = arqEntrada 
        self.numeroDeCidades = 0
        self.populacao = []
        self.cidades = []   #[[x,y], [x,y]]
        self.fitness = []
    
    def gerarPopulacaoIncial(self)->None:
        for _ in range(self.tamanhoPopulacao):
            populacao = [i for i in range(self.numeroDeCidades)]
            random.shuffle(populacao) 
            self.populacao.append(populacao)
        
    def calcularDistancia(self, x1:float, y1:float, x2:float, y2:float)->float: 
        x = x2 - x1 
        y = y2 - y2 
        sqr = (x*x) + (y*y) 
        return math.sqrt(sqr)

    def custoCaminho(self, caminho:List[int])->float: 
        total = 0
        for i in range(0, len(caminho)-1):
            total += self.calcularDistancia(self.cidades[caminho[i]][0], self.cidades[caminho[i]][1],
            self.cidades[caminho[i+1]][0], self.cidades[caminho[i+1]][1])

        return total

    def calcularFitness(self, populacao: List[List[int]])->None:
        for pop in populacao:
            self.fitness.append(1.0 / self.custoCaminho(pop)) 
    
    def selecaoPais(self)->int:
        #roleta
        pass  

    def cruzamento(self, pai1:List[int], pai2:List[int])->List[int]:
        #coinflip
        pass 

    def manutencao(self, filho:List[int])->None:
        #colocar o filho no lugar do pior, caso seja melhor
        pass 

    def lerEntrada(self)->None:
        c = 0 
        with open(self.arqEntrada) as file:
            for line in file:
                
                if c<6:
                    c+=1
                    continue

                line = line.strip() 
                aux = line.split(" ")
                if aux[0] == "EOF":
                    break
                aux = list(map(float, aux))
                self.cidades.append(aux[1:]) 
        
        print(self.cidades)

                

    def run(self)->float:
        self.lerEntrada()
        self.gerarPopulacaoIncial()
        self.calcularFitness()
        geracao = 0 
        while geracao < self.numeroGeracoes:

            pai1 = self.selecaoPais()
            pai2 = self.selecaoPais()

            filho = self.cruzamento(self.populacao[pai1], self.populacao[pai2])

            #gerar um numero aleatorio de 0 a 1 
            #mut = rand(0,1)
            #if mut <= taxa de mutacao:
            #fazer mutacao

            self.manutencao(filho)

            geracao+=1


def main():
    genetico = Ga(10, 0.1,100,'att48.txt')
    genetico.gerarPopulacaoIncial()
    genetico.lerEntrada()

if __name__ == "__main__":
    main()