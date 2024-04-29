from mod.estado import Estado


def _my_hash(matriz):
    """Função que calcula um valor hash para uma matriz de inteiros.
       Concatena os valores da matriz, da esquerda para a direita, de cima para baixo."""
    i = 0
    total = 0
    for linha in matriz:
        for valor in linha:
            total += valor * 10 ** i
            i += 1
    return total


class EstadoPuzzle(Estado):
    """Classe que representa um estado do problema do puzzle"""

    def __init__(self, matriz):
        """Construtor do estado do puzzle. Recebe uma matriz de inteiros,
           que representa a configuracao do estado"""
        self.__matriz = matriz

    def id_valor(self):
        # return hash(self.__matriz)
        return _my_hash(self.__matriz)
