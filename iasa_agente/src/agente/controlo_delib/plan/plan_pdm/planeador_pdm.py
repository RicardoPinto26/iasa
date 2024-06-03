from agente.controlo_delib.plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from agente.controlo_delib.plan.plan_pdm.plano_pdm import PlanoPDM
from agente.controlo_delib.plan.planeador import Planeador
from pdm.pdm import PDM


class PlaneadorPDM(Planeador):
    """Representa um planeador baseado no processo de decisao de Markov."""

    def __init__(self, gama=0.85, delta_max=1):
        """Construtor da classe."""
        self.__gama = gama
        self.__delta_max = delta_max

    def planear(self, modelo_plan, objectivos):
        """Gera o plano de accoes baseado na politica calculado atraves do processo de decisao de Markov."""
        if objectivos:
            modelo_pdm = ModeloPDMPlan(modelo_plan, objectivos)
            pdm = PDM(modelo_pdm, self.__gama, self.__delta_max)
            utilidade, politica = pdm.resolver()
            return PlanoPDM(utilidade, politica)
