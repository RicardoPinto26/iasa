from pee.melhor_prim.aval.heuristica import Heuristica


class HeuristicaContagem(Heuristica):
    """Heuristica da contagem."""

    def __init__(self, objetivo):
        """Construtor da classe"""
        self.__objetivo = objetivo

    def h(self, estado):
        """Heuristica que retorna a diferenca entre o objetivo e o valor atual, ou seja, a
        distancia entre o valor atual e o valor objetivo"""
        return abs(self.__objetivo - estado.valor)
