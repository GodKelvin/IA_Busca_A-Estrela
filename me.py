#Carregar arquivo com o grid posteriormente
from nbformat import read


def read_grid(path_file):
	grid = []
	with open(path_file) as file:
		#Lendo todas as linhas do arquivo de uma vez
		lines = file.readlines()
		for line in lines:
			#Removendo caracteres especiais(\n) e separando por espaco em branco
			line = line.strip().split(' ')
			#Convertendo os valores da linha para inteiro
			for i in range(len(line)):
				line[i] = int(line[i])
			grid.append(line)

	return grid

#Baseado na distancia de mannhatan
#Formula: |x1 - x2| + |y1 - y2|
#Ou para N dimensoes: SUM(1~N)|pi - qi|
def get_distance(p, q):
	distance = 0
	for p_i, q_i in zip(p, q):
		distance += abs(p_i - q_i)
	
	return distance

#Recebe o grid o objetivo
#Calcula a distancia de todos os pontos ate o objetivo
#Retorna a matriz com as heuristicas
def calc_heuristic(grid, end):
	heuristic = []
	for i in range(len(grid)):
		j = 0
		new_line = []
		for j in range(len(grid[i])):
			new_value = get_distance([i,j], end)
			new_line.append(new_value)
		heuristic.append(new_line)

	return heuristic

def print_grid(grid):
	for line in grid:
		print(line)
	print("\n")

def print_grid_t(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print("%d\t " %grid[i][j], end="")
		print("\n")
    

def search(grid, heuristic, start, end):
    lista_aberta = []
    lista_fechada = []


    #Contagem de nos expandidos
    custo_start = 0

    #inicilizando as listas
    for i in range(len(grid)):
        linha = []
        for j in range(len(grid[0])):
            linha.append(0)
        lista_aberta.append(linha)
        lista_fechada.append(linha)    

    #Soma da  heuristica + o custa inicial da cell
    custo_cell = heuristic[start[0]][start[1]] + custo_start

    #Informo que ja trabalhei com a minha posicao inicial
    lista_fechada[start[0]][start[1]] = 1
    
    bkp_cell = [[custo_cell, custo_start, start]]

    #flags
    achou = False
    expandir = True

    return 0

    

    



def main():
    path_grid = "grids/grid_2.txt"
    grid = read_grid(path_grid)
    start = [0,0]
    end = [4,5]
    heuristc = calc_heuristic(grid, end)
    print_grid(heuristc)
    best_path = search(grid, heuristc, start, end)


main()