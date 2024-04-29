from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim


class ProcuraInformada(ProcuraMelhorPrim):
    """
    Classe que representa uma procura informada.
    Uma procura informada e um metodo que tira partido de conhecimento do dominio do problema para
    ordenar a fronteira de exploracao. Este tipo de procura usa uma heuristica para guiar a exploracao,
    tendo assim um custo computacional menor.

    Nao existe atributo protegido heuristica.
    """

    def procurar(self, problema, heuristica):
        """Procura uma solucao, usando uma heuristica para guiar a exploracao."""
        self._avaliador.definir_heuristica(heuristica)

        return super().procurar(problema)
