from agente.controlo_delib.controlo_delib import ControloDelib
from agente.controlo_delib.plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae import Agente


class AgenteDelibPDM(Agente):
    """Classe que representa um Agente Deliberativo que utiliza um planeador
    por processo de decisão de Markov."""

    def __init__(self):
        # O valor 0.98 e usado para que o ambiente 4,5 e 6 sejam resolvidos
        # Para os outros ambientes, o gama por omissao (0.85) e suficiente
        planeador = PlaneadorPDM(0.98)
        controlo = ControloDelib(planeador)
        super().__init__(controlo)
