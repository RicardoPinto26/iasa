from mod.problema import Problema


class ProblemaPlan(Problema):
    """Representa um problema de planeamento."""
    def __init__(self, modelo_plan, estado_final):
        self.__estado_final = estado_final

        estado_inicial = modelo_plan.obter_estado()
        operadores = modelo_plan.obter_operadores()
        super().__init__(estado_inicial, operadores)

    def objectivo(self, estado):
        """Verifica se o estado e objectivo.
           Estado e objectivo se for o estado final."""
        return estado == self.__estado_final
