#Author: Kelvin Lehrback

#Para pegar os argumentos via linha de comando
import sys

#Para calcular o tempo de execucao
import time

from utils_grid import *
from a_star import a_estrela

#Responsavel por chamar os casos propostos no trabalho,
#e plotar o mapa do caminho, junto com as coordenadas
def run(grid, start, end):
    heuristic = calc_heuristic(grid, end)
    inicio = time.time()
    path = a_estrela(grid, heuristic, start, end)
    total = time.time() - inicio

    print("Tempo total: %.5f segundos" %total)
    if(path != None):
        print("Caminho encontrado: ")
        print(path)
        print("\n")
        print("Caminho desenhado:")
        print_path(grid, path, start, end)
    else:
        print("Nem um caminho encontrado / Caminho invalido")

def main():

    #Captura os valores do sistema
    path_grid = sys.argv[1]
    start_value = sys.argv[2].split(',')
    end_value = sys.argv[3].split(',')

    start = (int(start_value[0]), int(start_value[1]))
    end = (int(end_value[0]), int(end_value[1]))

    grid = read_grid(path_grid)
    print("Labirinto:")
    print_grid(grid)
    print("\n")
    #Caso 1
    print("Caso 1: (0,0), 13,12)")
    run(grid, (0,0), (13,12))

    #Caso 2
    print("Caso 2: (13,12), (0,0)")
    run(grid, (13,12), (0,0))

    #Caso 3
    print("Input do Usuario: ", start, end)
    run(grid, start, end)
    
main()