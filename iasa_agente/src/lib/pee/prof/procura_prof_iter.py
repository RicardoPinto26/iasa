from pee.prof.procura_prof_lim import ProcuraProfLim


class ProcuraProfIter(ProcuraProfLim):
    """Classe que implementa o mecanismo de procura em profundidade iterativa.

       Este tipo de procura utiliza a procura em profundidade limitada, aumentando o limite de
       profundidade a cada iteracao, ate que seja encontrada uma solucao, ou que o limite de
       profundidade seja atingido. Caso nao tenha limite de profundidade, e optima e completa,
       caso tenha limite, nao e nem completa nem optima, visto que a
       solucao (ou a solucao optima) pode estar a uma profundidade superior ao limite

       Complexidade Temporal: O(b^d)
       Complexidade Espacial: O(bd)

       sendo b o factor de ramificacao e d a dimensao da solucao."""

    def procurar(self, problema, inc_prof=1, limite_prof=1000):
        """Procura em profundidade iterativa."""
        for self.prof_max in range(0, limite_prof + 1, inc_prof):
            solucao = super().procurar(problema)
            if solucao:
                return solucao
