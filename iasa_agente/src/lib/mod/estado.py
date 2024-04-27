from abc import ABC, abstractmethod


class Estado(ABC):
    """Classe que representa um estado num problema de planeamento.
       Um estado representa uma configuracao de um sistema ou problema.
       Tem identificacao unica.
    """

    @abstractmethod
    def id_valor(self):
        """Define identificacao unica do estado em funcao da sua informacao (valor de estado)"""

    def __hash__(self):
        """Re-Define a funcao de hashing. Utiliza o id_valor para identificar o Estado"""
        return self.id_valor()

    def __eq__(self, other):
        """Re-Define a funcao de comparacao de igualdade.
           Algo é igual a um estado se: tambem for um estado e tiver o mesmo hash/id_valor"""
        return isinstance(other, Estado) and self.__hash__() == other.__hash__()
