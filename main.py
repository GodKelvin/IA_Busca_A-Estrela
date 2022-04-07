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

    #Verificando se os valores sao menores ou maiores, para
    #colocar na posicao correta da fila, com base no custo total
    def __lt__(self, other):
      return self.f < other.f
    
    def __gt__(self, other):
      return self.f > other.f

#Retornar o caminho correto dado um noh
#Sempre verificando qual era o seu parente
def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    
    #Retorna o caminho reverso (sort.reverse)
    return path[::-1]


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
        #Captura o menor noh para fins de verificacao
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        #Verifica se chegou ao fim
        if current_node == end_node:
            return return_path(current_node)

        #Caso contrario, cria uma lista para armazenar as novas posicoes
        children = []
        
        #Para cada posicao que o Noh pode se mover (Cima, baixo, direita cima)
        for new_position in move:

            #Calcula qual sera a nova posicao do noh com base no movimento
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            #Verifica se esta dentro dos limites do grid
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            #Verifica se nao eh um obstaculo
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            #Cria um novo noh, com base nessa nova posicao
            new_node = Node(current_node, node_position)

            #Salva essa posicao na lista de nos validos
            children.append(new_node)

        #Verifico a lista de nohs filhos
        for child in children:
            #Se o noh filho tiver caminho para ir
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            #Calculo os valores de 'g', 'h' e 'f'
            child.g = current_node.g + 1

            #Valor de 'h' com base na distancia de manhattan
            child.h = heuristic[child.position[0]][child.position[1]]
            child.f = child.g + child.h

            #se o noh filho ja estiver na lista aberta, 
            if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                continue

            #Coloca essa lista de nohs no topo da fila
            heapq.heappush(open_list, child)
        
    #Nao encontrou nem um caminho
    return None


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