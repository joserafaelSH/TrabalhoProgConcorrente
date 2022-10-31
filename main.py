import genetico

def main():
    arquivo = genetico.InputFile('att48.txt')
    arquivo.lerEntrada()

    gen = genetico.Genetic(0.3, 10000, 10, arquivo.get_input_size(), arquivo.get_city_points(), 'saida.txt', 1, 2)
    gen.run()

if __name__ == '__main__':
    main()