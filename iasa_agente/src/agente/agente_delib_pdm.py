from agente.controlo_delib.controlo_delib import ControloDelib
from agente.controlo_delib.plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae import Agente


class AgenteDelibPDM(Agente):
    """Classe que representa um Agente Deliberativo que utiliza um planeador
    por processo de decisão de Markov. TODO:"""

    def __init__(self):
        planeador = PlaneadorPDM()
        controlo = ControloDelib(planeador)
        super().__init__(controlo)
