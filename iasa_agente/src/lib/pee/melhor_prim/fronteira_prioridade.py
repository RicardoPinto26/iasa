from pee.mec_proc.fronteira import Fronteira


class FronteiraPrioridade(Fronteira):
    """Classe que representa uma fronteira de exploracao, onde os nos sao ordenados por prioridade.
       A prioridade para a ordenacao dos nos e dada pelo avaliador"""

    def __init__(self, avaliador):
        """Construtor da classe."""
        self.__avaliador = avaliador
        super().__init__()
        raise NotImplementedError

    def inserir(self, no):
        """Insere o no na fronteira, e ordena os nos por prioridade."""
        self._nos.append(no)
        self._nos.sort(key=lambda n: self.__avaliador.prioridade(n))
        self._nos.reverse()
        raise NotImplementedError

    def remover(self):
        """Remove o no com maior prioridade da fronteira, e retorna-o."""
        return self._nos.pop(0)
        raise NotImplementedError
