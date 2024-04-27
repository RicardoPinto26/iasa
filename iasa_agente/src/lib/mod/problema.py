from abc import ABC, abstractmethod


class Problema(ABC):
    """Classe que representa um problema de planeamento.
    Este e um tipo de problema onde a solucao consiste numa sequencia de accoes a realizar e de
    situacoes a percorrer para, partindo de uma situacao inicial, atingir uma situacao final (objectivo).
    """

    @property
    def estado_inicial(self):
        """Propriedade read only, que retorna o backing field.
           Contem o estado inicial do problema."""
        return self.__estado_inicial

    @property
    def operadores(self):
        """Propriedade read only, que retorna o backing field.
           Contem os operadores do problema."""
        return self.__operadores

    def __init__(self, estado_inicial, operadores):
        """Construtor da classe"""
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    @abstractmethod
    def objectivo(self, estado):
        """Identifica se o estado passado como argumento e um estado objectivo.
           Retorna true se for, false se nao."""
