from agente.controlo_delib.plan.plan_pdm.plano_pdm import PlanoPDM
from agente.controlo_delib.plan.planeador import Planeador
from pdm.pdm import PDM


class PlaneadorPDM(Planeador):
    def __init__(self, gama=0.85, delta_max=1):
        self.__gama = gama
        self.__delta_max = delta_max

    def planear(self, modelo_plan, objectivos):
        pdm = PDM(modelo_plan, self.__gama, self.__delta_max)
        utilidade, politica = pdm.resolver()
        return PlanoPDM(utilidade, politica)