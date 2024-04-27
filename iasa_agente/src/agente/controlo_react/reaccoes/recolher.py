from agente.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from agente.controlo_react.reaccoes.explorar.explorar import Explorar
from ecr.hierarquia import Hierarquia


class Recolher(Hierarquia):
    """Classe que representa um comportamento composto por hierarquia, para recolha de alvos."""

    def __init__(self):
        """Construtor da classe que cria a hierarquia de comportamentos"""
        comportamentos = [AproximarAlvo(), EvitarObst(), Explorar()]
        # comportamentos = [ContarPassos(), Explorar()]
        # comportamentos = [AproximarAlvo(), Explorar()]
        super().__init__(comportamentos)
