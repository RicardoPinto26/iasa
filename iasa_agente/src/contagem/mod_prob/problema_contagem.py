from mod_prob.estado_contagem import EstadoContagem
from mod_prob.operador_incremento import OperadorIncremento
from mod.problema import Problema


class ProblemaContagem(Problema):

    def __init__(self, valor_inicial, valor_objetivo, incrementos):
        """Construtor da classe"""
        super().__init__(
            EstadoContagem(valor_inicial),
            [OperadorIncremento(incremento) for incremento in incrementos]
        )
        self.__valor_objetivo = valor_objetivo

    def objectivo(self, estado):
        """Verifica se o estado é o objectivo, ou seja, se o valor objetivo ja foi alcancado"""
        return estado.valor >= self.__valor_objetivo
