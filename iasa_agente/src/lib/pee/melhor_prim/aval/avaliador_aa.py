from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur


class AvaliadorAA(AvaliadorHeur):
    """classe que representa um avaliador de procura A*."""

    def prioridade(self, no):
        """Retorna a prioridade do no.
           f(n) = g(n) + h(n)
           """
        return no.custo + self._heuristica.h(no.estado)
