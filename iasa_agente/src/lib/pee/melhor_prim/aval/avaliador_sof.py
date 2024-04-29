from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur


class AvaliadorSof(AvaliadorHeur):
    """classe que representa um avaliador de procura sofrega."""

    def prioridade(self, no):
        """Retorna a prioridade do no.
           f(n) = h(n)
           """
        return self._heuristica.h(no.estado)
