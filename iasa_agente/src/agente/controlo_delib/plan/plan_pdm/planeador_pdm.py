from agente.controlo_delib.plan.planeador import Planeador


class PlaneadorPDM(Planeador):
    def __init__(self, gama=0.85, delta_max=1):
        raise NotImplementedError

    def planear(self, modelo_plan, objectivos):
        raise NotImplementedError