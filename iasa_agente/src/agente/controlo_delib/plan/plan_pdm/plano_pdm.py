from agente.controlo_delib.plan.plano import Plano


class PlanoPDM(Plano):
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        return self.__politica[estado]

    def mostrar(self, vista):
        raise NotImplementedError
