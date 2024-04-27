from pee.prof.procura_profundidade import ProcuraProfundidade


class ProcuraProfLim(ProcuraProfundidade):
    """Classe que implementa o mecanismo de procura em profundidade limitada.

       Este tipo de procura limita a profundidade a que a arvore de procura e expandida, garantido
       que a procura nao encontra ciclos infinitos. Nao e completa nem optima, visto que a
       solucao (ou a solucao optima) pode estar a uma profundidade superior ao limite.

       Complexidade Temporal: O(b^l)
       Complexidade Espacial: O(bl)

       sendo b o factor de ramificacao e l o limite de profundidade.
       """
    @property
    def prof_max(self):
        """Getter de prof_max"""
        return self.__prof_max

    @prof_max.setter
    def prof_max(self, valor):
        """Setter de prof_max"""
        self.__prof_max = valor

    def __init__(self, prof_max=5):
        """Construtor da classe."""
        self.__prof_max = prof_max
        super().__init__()

    def _expandir(self, problema, no):
        """Expande um no, gerando os seus nos sucessores.
        So expande ate ao limite de profundidade."""
        if no.profundidade < self.prof_max:
            return super()._expandir(problema, no)
        return []
