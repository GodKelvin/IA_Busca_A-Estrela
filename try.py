# retorna o indice do menor elemento 
import numpy

#Carregar arquivo com o grid posteriormente
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


# funcao que encontra os caminhos possiveis a partir de um no
def expande_nos(pos, lista_fechada, lista_aberta, mat, xf, yf, g, custo):
	if pos[0] >= 0 and pos[0] < 15 and pos[1] >= 0 and pos[1] < 15 and mat[pos[0]][pos[1]] != 1:
			if pos not in lista_fechada and pos not in lista_aberta:
				#h = abs(xf - pos[0]) + abs(yf - pos[1])
				h = heuristic[pos[0]][pos[1]]
				g = g + 1
				lista_aberta.append(pos)
				custo.append(g+h)


def print_grid(grid):
	for line in grid:
		print(line)
	print("\n")

def heuristica(mat, xi, yi, xf, yf):
	g = 0
	#h = (xf - xi) + (yf - yi)
	h = heuristic[xi][yi]
	destino = [xf, yf]

	# matriz que direciona os possiveis caminhos do ponto atual
	delta = [[-1, 0],   # cima
			 [0, -1],   # esquerda
			 [1, 0],    # baixo
			 [0, 1]]    # direita
	
	caminho = []
	atual = [xi, yi]
	l_fechada = []
	l_aberta = [[xi, yi]]
	custo = [[g+h]]
	
	while len(l_aberta) > 0 and atual != destino:	
		menor_indice = numpy.argmin(custo)
		atual = l_aberta[menor_indice]
		del l_aberta[menor_indice]
		del custo[menor_indice]
		l_fechada.append(atual)
		
		cima = [atual[0]+delta[0][0], atual[1]+delta[0][1]]
		esquerda = [atual[0]+delta[1][0], atual[1]+delta[1][1]]
		baixo = [atual[0]+delta[2][0], atual[1]+delta[2][1]]
		direita = [atual[0]+delta[3][0], atual[1]+delta[3][1]]

		expande_nos(cima, l_fechada, l_aberta, mat, xf, yf, g, custo)	
		expande_nos(esquerda, l_fechada, l_aberta, mat, xf, yf, g, custo)
		expande_nos(baixo, l_fechada, l_aberta, mat, xf, yf, g, custo)
		expande_nos(direita, l_fechada, l_aberta, mat, xf, yf, g, custo)
		
		caminho.append(atual)

	for coord in caminho:
		mat[coord[0]][coord[1]] = 9
	
	print_grid(mat)

	print(caminho)


path_grid = "grids/grid_1.txt"
grid = read_grid(path_grid)
start = [0,0]
end = [13,12]
heuristic = calc_heuristic(grid, end)

def main():	
	print_grid(heuristic)
	heuristica(grid, start[0], start[1], end[0], end[1])


	
main()
