from pee.melhor_prim.aval.avaliador import Avaliador


class AvaliadorCustoUnif(Avaliador):
    """Classe que representa um avaliador de custo uniforme.
       A prioridade e ditada pelo custo acumulado do no."""

    def prioridade(self, no):
        """Devolve a prioridade do no
        A prioridade e igual ao custo acumulado do no.
        """
        return no.custo
