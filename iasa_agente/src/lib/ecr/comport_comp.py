from abc import abstractmethod

from .comportamento import Comportamento


class ComportamentoComp(Comportamento):
    """Classe que representa um comportamento composto.
        Um comportamento composto agrega conjuntos de comportamentos.
    """

    def __init__(self, comportamentos):
        """Construtor da classe ComportamentoComp"""
        self.__comportamentos = comportamentos

    def activar(self, percepcao):
        """Activa o comportamento, retornando a accao que corresponde a percepcao
            Neste caso, activa todos os comportamentos internos, e seleciona a accao a retornar
        """
        accoes = []
        for comportamento in self.__comportamentos:
            accao = comportamento.activar(percepcao)
            if accao:
                accoes.append(accao)

        if accoes:
            return self.seleccionar_accao(accoes)

    @abstractmethod
    def seleccionar_accao(self, accoes):
        """determina a acção a realizar em funçao das respostas dos varios comportamentos internos"""
