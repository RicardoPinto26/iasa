from mod.estado import Estado


class EstadoAgente(Estado):
    """Classe que representa um estado para o agente. Este estado tem uma posicao."""

    @property
    def posicao(self):
        return self.__posicao

    def __init__(self, posicao):
        self.__posicao = posicao

    def id_valor(self):
        return hash(self.__posicao)
