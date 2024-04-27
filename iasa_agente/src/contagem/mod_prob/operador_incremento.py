from mod_prob.estado_contagem import EstadoContagem
from mod.operador import Operador


class OperadorIncremento(Operador):
    @property
    def incremento(self):
        return self.__incremento

    def __init__(self, incremento):
        """Construtor da classe. Guarda o incremento a aplicar."""
        self.__incremento = incremento

    def custo(self, estado, estado_suc):
        """Custo = incremento ao quadrado."""
        return self.__incremento ** 2

    def aplicar(self, estado):
        """Aplica o incremento ao estado e devolve o novo estado."""
        return EstadoContagem(estado.valor + self.__incremento)
