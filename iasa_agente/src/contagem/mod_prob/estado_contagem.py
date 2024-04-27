from mod.estado import Estado


class EstadoContagem(Estado):
    @property
    def valor(self):
        """Valor da contagem."""
        return self.__valor

    def __init__(self, valor):
        """Construtor da classe."""
        self.__valor = valor

    def id_valor(self):
        """Retorna o hash do valor da contagem."""
        return hash(self.__valor)
