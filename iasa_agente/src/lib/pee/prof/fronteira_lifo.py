from pee.mec_proc.fronteira import Fronteira


class FronteiraLIFO(Fronteira):
    """Classe que representa uma fronteira de exploracao.
       A insercao nos nos e feita no inicio da lista, de forma a garantir o comportamento LIFO.
       """

    def inserir(self, no):
        self._nos.insert(0, no)
