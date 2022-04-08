#Para fins de prioridade do Noh, utilizei o heapq, cujo tutorial vi em:
import heapq ##https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

#importando a classe de No
from node import Node

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