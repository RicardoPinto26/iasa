from pee.larg.procura_grafo import ProcuraGrafo
from pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade


class ProcuraMelhorPrim(ProcuraGrafo):
    """Classe que implementa o mecanismo de procura em grafo, para procura melhor primeiro.
       A procura melhor primeiro e uma procura de grafo, onde o grafo expandido, ou seja, o primeiro
       da fronteira, e o no com maior prioridade. A prioridade e determinada por um avaliador.
    """

    def __init__(self, avaliador):
        """Construtor da classe."""
        self._avaliador = avaliador
        super().__init__(FronteiraPrioridade(avaliador))

    def _manter(self, no):
        # Se a procura em grafo ja mantem o no, ou se o custo do no for menor que o custo ja explorado,
        # retorna True, caso contrario, retorna False.
        return super()._manter(no) or no.custo < self._explorados[no.estado].custo
