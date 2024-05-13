from agente.controlo_delib.modelo.modelo_plan import ModeloPlan


class ModeloPDMPlan(ModeloPlan):
    def __init__(self, modelo_plan, objectivos, rmax=1000):
        self.__modelo_plan = modelo_plan
        raise NotImplementedError

    def obter_estado(self):
        raise NotImplementedError

    def obter_estados(self):
        raise NotImplementedError

    def obter_operadores(self):
        raise NotImplementedError

    def S(self):
        raise NotImplementedError

    def A(self, s):
        raise NotImplementedError

    def T(self, s, a, sn):
        raise NotImplementedError

    def R(self, s, a, sn):
        raise NotImplementedError

    def suc(self, s, a):
        raise NotImplementedError
