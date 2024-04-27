from ecr.estimulo import Estimulo


class EstimuloObst(Estimulo):
    """Classe que representa um estimulo de obstaculo"""

    def __init__(self, direccao, intensidade=1):
        """Construtor da classe"""
        self.__direccao = direccao
        self.__intensidade = intensidade

    def detectar(self, percepcao):
        """Calcula a intensidade da percepcao. self.__intensidade se houver contacto com um obstaculo,
        0 caso contrario
        """
        if percepcao.contacto_obst(self.__direccao):
            return self.__intensidade
        return 0
