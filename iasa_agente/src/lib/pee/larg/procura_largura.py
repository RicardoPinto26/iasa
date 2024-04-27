from pee.larg.fronteira_fifo import FronteiraFIFO
from pee.larg.procura_grafo import ProcuraGrafo


class ProcuraLargura(ProcuraGrafo):
    """Classe que implementa o mecanismo de procura em grafo, para procura em largura.
       Na procura em largura, o criterio de exploracao e a menor profundidade, ou seja,
       os nos mais antigos sao explorados primeiro. Isto representa uma fronteira onde os nos
       sao explorados por FIFO (first in, first out).

       Este tipo de procura ocupa mais memoria que a procura por largura, mas em contra partida,
       e completo e optimo. Ou seja, garante que encontra uma solucao, e que essa solucao e a
       melhor solucao possivel.

       Complexidade Temporal: O(b^d)
       Complexidade Espacial: O(b^d)

       sendo b o factor de ramificacao e d a dimensao da solucao."""
    def __init__(self):
        """Construtor da classe."""
        super().__init__(FronteiraFIFO())
