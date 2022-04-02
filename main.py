#Carregar arquivo com o grid posteriormente
def read_grid():
	grid = [[0, 1, 0, 0, 0, 0],
			[0, 1, 0, 0, 0, 0],
			[0, 1, 0, 0, 0, 0],
			[0, 1, 0, 0, 0, 0],
			[0, 0, 0, 0, 1, 0],]
	
	return grid


#Calcular o custo com base no grid(Passar tamanho tambem?)
def calc_heuristc():
	heuristic =	[[9, 8, 7, 6, 5, 4],
			  	 [8, 7, 6, 5, 4, 3],
				 [7, 6, 5, 4, 3, 2],
				 [6, 5, 4, 3, 2, 1],
				 [5, 4, 3, 2, 1, 0],]


def print_grid(grid):
	for line in grid:
		print(line)


def main():
	grid = read_grid()
	print_grid(grid)

	#Definindo os pontos de partida, destino e o custo
	start = [0,0]
	end = [4, 5] #Ou seja, os extremos do grid
	cost = 1

	#Definindo os movimentos do agente e a traducao dos mesmos
	deltar = [[-1, 0], #Cima
			  [0, -1], #Esquerda
			  [1,  0], #Baixo
			  [0,  1]] #Direita

	delta_name = ['^', '<', 'v', '>']
	


main()