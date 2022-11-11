#include<iostream>
#include <thread>
#include "utils.cpp"
#include <unistd.h>

std::string fileName = "att48.txt";

void thread1(){
    std::string outputFile = "saidaThread1.txt";
    fileReader::Reader entrada(fileName);
    entrada.readFile();
    Ga::Genetic genetico(0.1, 50000, entrada.get_cityPoints() , entrada.get_inputSize(), 25, outputFile, 0, 1 );
    genetico.run();
    std::cout<<"Fim da thread1"<<std::endl;
}

void thread2(){
    std::string outputFile = "saidaThread2.txt";
    fileReader::Reader entrada(fileName);
    entrada.readFile();
    Ga::Genetic genetico(0.3, 10000, entrada.get_cityPoints() , entrada.get_inputSize(), 10, outputFile, 0, 2 );
    genetico.run();
    std::cout<<"Fim da thread2"<<std::endl;
}

void thread3(){
    std::string outputFile = "saidaThread3.txt";
    fileReader::Reader entrada(fileName);
    entrada.readFile();
    Ga::Genetic genetico(0.2, 10000, entrada.get_cityPoints() , entrada.get_inputSize(), 50, outputFile, 1,3);
    genetico.run();
    std::cout<<"Fim da thread3"<<std::endl;
}

void thread4(){
    std::string outputFile = "saidaThread4.txt";
    fileReader::Reader entrada(fileName);
    entrada.readFile();
    Ga::Genetic genetico(0.7, 10000, entrada.get_cityPoints() , entrada.get_inputSize(), 5, outputFile, 1,4);
    genetico.run();
    std::cout<<"Fim da thread4"<<std::endl;
}

void (*ponteirodefuncao[4])() = {thread1,thread2,thread3,thread4};

int main(){
    try
    {
        std::vector<std::thread> threadsList;

        for(int i = 0; i< 4; i++)
            threadsList.push_back(std::thread(ponteirodefuncao[i]));
        
        for(int i = 0; i< 4; i++)
            threadsList[i].join();
    }
    catch (const std::exception &ex)
    {
        std::cout << "Deu merda" << ex.what() << "\n";
    }
    
    return 0 ;
}