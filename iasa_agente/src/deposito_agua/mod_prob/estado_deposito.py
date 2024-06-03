from mod.estado import Estado


class EstadoDeposito(Estado):

    @property
    def volume(self):
        return self.__volume

    def __init__(self, volume):
        self.__volume = volume

    def id_valor(self):
        return self.__volume
