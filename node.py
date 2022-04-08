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

    #Os metodos dessa classe (Noh) foram criados conforme tutorial:
    #https://www.tutorialspoint.com/How-to-implement-Python-lt-gt-custom-overloaded-operators
    #Para fins de comparacao com o mesmo tipo de classe
    
    #Para verificar se os nohs tem a mesma posicao
    def __eq__(self, other):
        return self.position == other.position

    #Para verificar se os valores sao menores ou maiores, com base no custo total de cada noh
    def __lt__(self, other):
      return self.f < other.f
    
    def __gt__(self, other):
      return self.f > other.f