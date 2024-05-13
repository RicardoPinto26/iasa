import math

from pee.melhor_prim.aval.heuristica import Heuristica


class HeurDist(Heuristica):
    """Representa uma heuristica de distancia."""

    def __init__(self, estado_final):
        self.__estado_final = estado_final

    def h(self, estado):
        """Calcula a estimativa de custo. Neste caso, a distancia entre o estado atual e o estado final."""
        return math.dist(estado.posicao, self.__estado_final.posicao)
