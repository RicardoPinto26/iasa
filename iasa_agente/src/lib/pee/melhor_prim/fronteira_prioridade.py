from heapq import heappush, heappop

from pee.mec_proc.fronteira import Fronteira


class FronteiraPrioridade(Fronteira):
    """Classe que representa uma fronteira de exploracao, onde os nos sao ordenados por prioridade.
       A prioridade para a ordenacao dos nos e dada pelo avaliador"""

    def __init__(self, avaliador):
        """Construtor da classe."""
        # Avaliador muda para protected
        self._avaliador = avaliador
        super().__init__()

    def inserir(self, no):
        """Insere o no na fronteira, de forma ordenada pela sua prioridade."""
        prioridade = self._avaliador.prioridade(no)
        heappush(self._nos, (prioridade, no))

    def remover(self):
        """Remove o no com maior prioridade da fronteira, e retorna-o.
           Caso a fronteira esteja vazia, e lancado um IndexError.
        """
        _, no = heappop(self._nos)
        return no
