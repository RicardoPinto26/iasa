from .comportamento import Comportamento


class Reaccao(Comportamento):
    """Classe que representa uma reaccao, que associa estimulos a respostas"""

    def __init__(self, estimulo, resposta):
        """Construtor da classe Reaccao"""
        self.__estimulo = estimulo
        self.__resposta = resposta

    def activar(self, percepcao):
        """Activa a reaccao, detectando a intensidade do estimulo, e activando a resposta se necessario"""
        intensidade = self.__estimulo.detectar(percepcao)
        if intensidade > 0:
            accao = self.__resposta.activar(percepcao, intensidade)
            return accao
