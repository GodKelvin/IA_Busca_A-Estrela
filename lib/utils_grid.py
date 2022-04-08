#Recebe o caminho do arquivo do grid
#Retorna uma matriz com base nos valores do grid
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

#Mostra na tela de forma limpa uma matriz
def print_grid(grid):
	for line in grid:
		print(line)
	print("\n")


#Dado o grid, uma lista de coordenadas (caminho),
#posicao inicial e posicao final:
#Mostra na tela de forma "bonita" o caminho realizado ->
#Sendo  @ == posicao inicial
#       x == posinal final
#      ' '== caminho livre
#       # == obstaculo
#       * == trajeto
def print_path(grid, path, start, end):
    grid_path = []

    #Criando o grid_path vazio
    for i in range(len(grid)):
        line = []
        for j in range(len(grid[i])):
            if(grid[i][j] == 0):
                #Caminho livre
                line.append(' ')
            else:
                #Obstaculo
                line.append('#')
        grid_path.append(line)

    # '@' = Inicio
    # 'x' = Fim
    grid_path[start[0]][start[1]] = '@'
    grid_path[end[0]][end[1]] = 'x'

    #Apagando as primeiras e ultimas posicoes do path,
    #visto que ja foram computadas no grid_path
    del path[0]
    del path[len(path) -1]
    for coord in path:
        grid_path[coord[0]][coord[1]] = '*'


    print_grid(grid_path)

#Baseado na distancia de mannhatan
#Formula: |x1 - x2| + |y1 - y2|
#Ou para N dimensoes: SUM(i=1~~N)|pi - qi|
def get_distance(p, q):
	distance = 0
    #Funcao ZIP retorna uma lista de tuplas
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