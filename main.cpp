#include<iostream>
#include "utils.cpp"

std::string fileName = "att48.txt";

int main(){

    //fazer 4 threads
    //2 configuracoes de parametros para cada cruzamento: geracoes, mutacao
    //executar as threads 
    //dar o join para esperar o final de todas
    //cada thread escreve em um arquivo sua saida 
    //grafico de como a resposta do genetico evoluiu para cada thread 
    //relatorio

    //config1: geracoes, mutacao , cruzamento ox
    //config2: geracoes, mutacao , cruzamento ox
    //config3: geracoes, mutacao , cruzamento cx
    //config4: geracoes, mutacao , cruzamento cx


    //exemplo de uma execucao
    fileReader::Reader entrada(fileName);
    entrada.readFile();
    std::vector<std::vector<float>> c =  entrada.get_cityPoints();
    Ga::Genetic genetico(0.1, 50000,c , entrada.get_inputSize(), 25);
    genetico.run();

   
    
    return 0 ;
}