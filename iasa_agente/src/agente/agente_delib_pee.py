from agente.controlo_delib.controlo_delib import ControloDelib
from agente.controlo_delib.plan.plan_pee.planeador_pee import PlaneadorPEE
from sae import Agente


class AgenteDelibPEE(Agente):
    """Classe que representa um Agente Deliberativo.
       A arquitetura de um agente deliberativo e baseada em representacoes internas
       do dominio do problema, nas quais e possivel explorar as opcoes possiveis por simulacao interna,
       para atingir objectivos explicitamente representados, tendo por base processos de
       deliberacao sobre que objectivos concretizar e quais os meios a utilizar.
    """

    def __init__(self):
        planeador = PlaneadorPEE()
        controlo = ControloDelib(planeador)
        super().__init__(controlo)
