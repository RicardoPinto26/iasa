from pee.melhor_prim.aval.avaliador import Avaliador


class AvaliadorHeur(Avaliador):
    """Classe abstrata que define a interface de um avaliador de nos com base numa heuristica"""

    def definir_heuristica(self, heuristica):
        """Define a heuristica a ser utilizada"""
        self._heuristica = heuristica
