import heapq
import sys

class Node:
    
    #Recebe como argumento o no parente e a posicao
    #O no parente eh necessario para "voltar" ao inicio
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        #Valores iniciais de G, H e F,
        #sendo:
            # f = Custo total do noh
            # g = Distancia do noh atual ate o noh inicial
            # h = distancia do noh atual ate o noh final
        self.g = 0
        self.h = 0
        self.f = 0

    #
    def __eq__(self, other):
        return self.position == other.position
    
    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f

def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


#Recebe como argumento:
    #Grid de caminho
    #Grid da heuristica de cada posicao no grid de caminhos
    #Posicao inicial e final
def a_estrela(maze, heuristic, start, end):

    #Cria o no inicial e final
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    #Iniciando as listas abertas e fechadas
    open_list = []
    closed_list = []

    #Iniciando a pilha e colocando o no inicial
    heapq.heapify(open_list) 
    heapq.heappush(open_list, start_node)
	
    # matriz que direciona os possiveis caminhos do ponto atual
    move = ((0, -1), #Esquerda
                        (0, 1),  #Direita
                        (-1, 0), #Cima
                        (1, 0))  #Baixo

    #Enquanto tiver nos que nao foram verificados, procure!
    while len(open_list) > 0:   
        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate children
        children = []
        
        for new_position in move: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            #child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.h = heuristic[child.position[0]][child.position[1]]
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)
        
    #Nao encontrou nem um caminho
    return None

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

def print_grid(grid):
	for line in grid:
		print(line)
	print("\n")

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


#Responsavel por chamar os casos propostos no trabalho,
#e plotar o mapa do caminho, junto com as coordenadas
def run(grid, start, end):
    heuristic = calc_heuristic(grid, end)
    path = a_estrela(grid, heuristic, start, end)
    if(path != None):
        print("Caminho encontrado: ")
        print(path)
        print("\n")
        print("Caminho desenhado:")
        print_path(grid, path, start, end)
    else:
        print("Nem um caminho encontrado / Caminho invalido")

def main():
    #path_grid = "grids/grid_1.txt"
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
    print("Caso 1: ")
    run(grid, (0,0), (13,12))

    #Caso 2
    print("Caso 2: ")
    run(grid, (13,12), (0,0))

    #Caso 3
    print("Input do Usuario:")
    run(grid, start, end)

    

    
main()