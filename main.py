


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

# grid, pos_inicial e destino
def search(grid, heuristic, init, goal):

	#Custo de cada acao
	cost = 1

	#Definindo os movimentos do agente e a traducao dos mesmos
	delta = [[-1, 0], #Cima
			  [0, -1], #Esquerda
			  [1,  0], #Baixo
			  [0,  1]] #Direita

	#Informacao dos nos ou posicoes que foram expandidos ou nao
	closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
	closed[init[0]][init[1]] = 1

	#Contem a ordem crescente com que os nos foram expandidos
	expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

	#Receberam os movimentos realizados ate chegar ao ponto de destino
	action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

	#Ira desenhar a tragetoria do agente
	path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
	
	x = init[0]				#Seta a posicao inicial do agente em x
	y = init[1] 			#Seta a posicao inicial do agente em y
	g = 0 					#Seta o valor inicial da funcao em g
	f = g + heuristic[x][y] #Seta o valor inicial de f

	#Cria o vetor para guardar os componentes
	open = [[f, g, x, y]]
	
	#Criacao das flags para checar se ja encontrou o melhor caminho,
	#ou se ainda existem nos para expandir
	found = False
	resign = False

	#Contagem de nos expandidos
	count = 0

	#Caso a busca nao esteja completa e ainda ha nos para expandir
	while not found and not resign:
		#Se nao houve nos para expandir, nao encontrou o melhor caminho, fim
		if(len(open) == 0):
			resign = True
			print(">>>CAMINHO NAO ENCONTRADO OU BLOQUEADO<<<\n\n")
			return 'fail'
		
		#Caso ainda tenha nos ha serem expandidos
		else:
			#ordenar o vetor open para verificar qual o proximo ponto
			open.sort()

			#Inverte a ordenacao
			open.reverse()

			#Recebe o valor extraido de open(melhor resultado)
			next = open.pop()
			f = next[0]
			g = next[1]
			x = next[2]
			y = next[3]

			#No expandido recebe sua contagem
			expand[x][y] = count

			#Acrescido em 1 o valor de nos expandidos
			count += 1

			#Caso chegou ao objetivo
			if(x == goal[0] and y == goal[1]):
				found = True
			else:
				#Movimenta o agente
				for i in range(len(delta)):
					x2 = x + delta[i][0]
					y2 = y + delta[i][1]

					#Verificando se a proxima posicao esta dentro do grid
					if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):

						#Verificando se o no relativo a posicao ainda nao foi expandido
						if(closed[x2][y2] == 0 and grid[x2][y2] == 0):
							g2 = g + cost					#'g' atual + novo custo da operacao
							f2 = g2 + heuristic[x2][y2]		#'f' recebe novo custo da operacao
							open.append([f2, g2, x2, y2])	# Salva os novos valores calculados
							#ORIGINAL
							#closed[x2][y2] = 1				# Sinaliza que o no ja foi expandido
							closed[x][y] = 1
							action[x][y] = i				# Sinaliza qual foi a acao tomada na posicao
	

	# delta = [[-1, 0], #Cima
	# 		  [0, -1], #Esquerda
	# 		  [1,  0], #Baixo
	# 		  [0,  1]] #Direita

	# x = 0
	# y = 0
	x = init[0]
	# y = init[1]

	# delta_name = ['^', '<', 'v', '>']
	# path[goal[0]][goal[1]] = '*'
	# while(x != goal[0] or y != goal[1]):
	# 	x2 = x + delta[action[x][y]][0]
	# 	y2 = y + delta[action[x][y]][1]

	# 	path[x][y] = delta_name[action[x][y]]
	# 	x = x2
	# 	y = y2
	return expand




def main():
	path_grid = "grids/grid_1.txt"
	grid = read_grid(path_grid)
	start = [0,0]
	end = [6,6]
	heuristic = calc_heuristic(grid, end)
	best_path = search(grid, heuristic, start, end)
	print_grid(best_path)
main()