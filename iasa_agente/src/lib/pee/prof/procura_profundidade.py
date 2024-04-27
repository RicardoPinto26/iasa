from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.prof.fronteira_lifo import FronteiraLIFO


class ProcuraProfundidade(MecanismoProcura):
    """Classe que implementa o mecanismo de procura, para procura em profundidade.
       Na procura em profundidade, o criterio de exploracao e a maior profundidade, ou seja,
       os nos mais recentes sao explorados primeiro. Isto representa uma fronteira onde os nos
       sao explorados por LIFO (last in, first out).

       Este tipo de procura ocupa menos memoria que a procura por largura, mas nao e nem otima
       nem completa. Ou seja, nao garante encontrar a solucao, e se a encontrar, nao garante que
       esta seja a melhor solucao possivel.

       Complexidade Temporal: O(b^m)
       Complexidade Espacial: O(bm)

       sendo b o factor de ramificacao e m a profundidade maxima da arvore de procura.
       """
    def __init__(self):
        """Construtor da classe."""
        super().__init__(FronteiraLIFO())

    def _memorizar(self, no):
        """Memoriza um no, ou seja, insere o no na fronteira."""
        self._fronteira.inserir(no)
