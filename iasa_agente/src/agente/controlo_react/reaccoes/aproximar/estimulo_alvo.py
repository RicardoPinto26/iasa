from ecr.estimulo import Estimulo
from sae import Elemento


class EstimuloAlvo(Estimulo):
    """Classe que representa um estimulo de alvo"""

    def __init__(self, direccao, gama=0.9):
        """Construtor da classe"""
        self.__gama = gama
        self.__direccao = direccao

    def detectar(self, percepcao):
        """Calcula a intensidade da percepcao atraves da distancia do alvo,
        usando uma funcao de decaimento exponencial
        """
        elemento, distancia, _ = percepcao[self.__direccao]
        if elemento == Elemento.ALVO:
            return self.__gama ** distancia
        return 0.0
