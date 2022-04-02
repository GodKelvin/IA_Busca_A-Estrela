#Carregar arquivo com o grid posteriormente
def read_grid():
	grid = [[0, 1, 0, 0, 0, 0],
			[0, 1, 0, 0, 0, 0],
			[0, 1, 0, 0, 0, 0],
			[0, 1, 0, 0, 0, 0],
			[0, 0, 0, 0, 1, 0]]
	
	return grid


#Calcular o custo com base no grid(Passar tamanho tambem?)
def calc_heuristic():
	heuristic =	[[9, 8, 7, 6, 5, 4],
			  	 [8, 7, 6, 5, 4, 3],
				 [7, 6, 5, 4, 3, 2],
				 [6, 5, 4, 3, 2, 1],
				 [5, 4, 3, 2, 1, 0]]

	# heuristic =	[[2, 1, 0, 1, 2, 3],
	# 		  	 [3, 2, 1, 2, 3, 4],
	# 			 [4, 3, 2, 3, 4, 5],
	# 			 [5, 4, 3, 4, 5, 6],
	# 			 [6, 5, 4, 5, 6, 7]]

	return heuristic


def print_grid(grid):
	for line in grid:
		print(line)



# grid, pos_inicial e destino
#def search(grid, init, goal):
def search():

	grid = read_grid()
	#print_grid(grid)

	#Definindo os pontos de partida, destino e o custo
	init = [0, 0]
	goal = [4, 5] #Ou seja, os extremos do grid
	#goal = [len(grid) - 1, len(grid[0]) - 1] #Ou seja, os extremos do grid
	print("Objetivo: ")
	print(goal[0], goal[1])
	#print(len(grid) - 1, len(grid[0]) - 1)
	cost = 1

	#Definindo os movimentos do agente e a traducao dos mesmos
	delta = [[-1, 0], #Cima
			  [0, -1], #Esquerda
			  [1,  0], #Baixo
			  [0,  1]] #Direita

	delta_name = ['^', '<', 'v', '>']

	############################################

	#Informacao dos nos ou posicoes que foram expandidos ou nao
	closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
	closed[init[0]][init[1]] = 1

	#Contem a ordem crescente com que os nos foram expandidos
	expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

	#Receberam os movimentos realizados ate chegar ao ponto de destino
	action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

	#Ira desenhar a tragetoria do agente
	path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

	print("\nCaminho Limpo:")
	print_grid(path)

	heuristic = calc_heuristic()
	print("\nHeuristica: ")
	print_grid(heuristic)
	
	x = init[0]				#Seta a posicao inicial do agente em x
	y = init[1] 			#Seta a posicao inicial do agente em y
	g = 0 					#Seta o valor inicial da funcao em g
	f = g + heuristic[x][y] #Seta o valor inicial de f
	print("\nf: %d" %(f))

	#Cria o vetor para guardar os componentes
	open = [[f, g, x, y]]
	
	print("Open: ", open)

	#Criacao das flags para checar se ja encontrou o melhor caminho,
	#ou se ainda existem nos para expandir
	found = False
	resign = False

	#Contagem de nos expandidos
	count = 0

	#Caso a busca nao esteja completa e ainda ha nos para expandir
	while not found and not resign:
		print("OPEN: ")
		print(open)
		print(count)
		#Se nao houve nos para expandir, nao encontrou o melhor caminho, fim
		if(len(open) == 0):
			resign = True
			print("FALHOU")
			return 'fail'
		
		#Caso ainda tenha nos ha serem expandidos
		else:
			#ordenar o vetor open para verificar qual o proximo ponto
			open.sort()

			print("SORT: ", open)
			#Inverte e ordenacao
			open.reverse()

			#Recebe o valor extraido de open(melhor resultado)
			next = open.pop()
			print("NEXT: ", next)
			f = next[0]
			g = next[1]
			x = next[2]
			y = next[3]

			#No expandido recebe sua contagem
			expand[x][y] = count

			#Acrescido em 1 o valor de nos expandidos
			count += 1
			print("COUNT: ", count)

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
							closed[x2][y2] = 1				# Sinaliza que o no ja foi expandido
							action[x][y] = i				# Sinaliza qual foi a acao tomada na posicao
	
	# x = 0
	# y = 0
	x = init[0]
	y = init[1]

	
	print_grid(expand)
	print("\n")

	print("DELTA: ")
	print_grid(delta)

	print("\nACITON: ")
	print_grid(action)
	while(x != goal[0] or y != goal[1]):
		print(x, y)
		x2 = x + delta[action[x][y]][0]
		y2 = y + delta[action[x][y]][1]

		path[x][y] = delta_name[action[x][y]]
		x = x2
		y = y2
	path[goal[0]][goal[1]] = '*'

	print_grid(path)
	
	return expand



def main():
	# grid = read_grid()
	# print_grid(grid)

	# #Definindo os pontos de partida, destino e o custo
	# init = [0,0]
	# goal = [4, 5] #Ou seja, os extremos do grid
	# cost = 1

	# #Definindo os movimentos do agente e a traducao dos mesmos
	# delta = [[-1, 0], #Cima
	# 		  [0, -1], #Esquerda
	# 		  [1,  0], #Baixo
	# 		  [0,  1]] #Direita

	# delta_name = ['^', '<', 'v', '>']
	search()



main()