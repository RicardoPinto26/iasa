from agente.controlo_delib.plan.plano import Plano


class PlanoPDM(Plano):
    def __init__(self, utilidade, politica):
        raise NotImplementedError

    def obter_accao(self, estado):
        raise NotImplementedError

    def mostrar(self, vista):
        raise NotImplementedError
