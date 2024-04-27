from pee.melhor_prim.avaliador import Avaliador


class AvaliadorCustoUnif(Avaliador):
    """Classe que representa um avaliador de custo uniforme.
       A prioridade e ditada pelo custo acumulado do no."""
    def prioridade(self, no):
        return no.custo
        raise NotImplementedError