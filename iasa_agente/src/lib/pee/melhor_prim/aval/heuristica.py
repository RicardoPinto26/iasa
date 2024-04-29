from abc import ABC, abstractmethod


class Heuristica(ABC):
    """Interface que define uma heuristica.
       Uma heuristica representa uma estimativa do custo do percurso desde o no atual até ao nó objectivo.
       A estimativa e independente do custo percorrido ate ao momento.
    """
    @abstractmethod
    def h(self, estado):
        """Devolve a estimativa de custo"""
