from mod_prob.estado_deposito import EstadoDeposito
from mod_prob.operador_encher import OperadorEncher
from mod_prob.operador_vazar import OperadorVazar

from mod.problema import Problema


class ProblemaDeposito(Problema):
    def __init__(self, volume_inicial, volume_objectivo):
        super().__init__(
            EstadoDeposito(volume_inicial),
            [OperadorEncher(2), OperadorEncher(3), OperadorVazar(2), OperadorVazar(3)]
        )
        self.__volume_objectivo = volume_objectivo

    def objectivo(self, estado):
        return estado.volume == self.__volume_objectivo
