from pee.mec_proc.fronteira import Fronteira


class FronteiraFIFO(Fronteira):
    """Classe que representa uma fronteira de exploracao.
       A insercao nos nos e feita no final da lista, de forma a garantir o comportamento FIFO.
       """

    def inserir(self, no):
        self._nos.append(no)
