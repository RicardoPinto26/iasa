from abc import abstractmethod, ABC

from mod.operador import Operador


class OperadorTransferir(Operador, ABC):
    """Operador que transfere"""

    @property
    def volume_transferido(self):
        return self.__volume_transferido

    def __init__(self, volume_transferido):
        self.__volume_transferido = volume_transferido

    def custo(self, estado, estado_suc):
        return (estado_suc.volume - estado.volume) ** 2

    @abstractmethod
    def aplicar(self, estado):
        """"""
