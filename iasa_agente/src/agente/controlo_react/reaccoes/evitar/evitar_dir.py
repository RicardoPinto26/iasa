from agente.controlo_react.reaccoes.evitar.estimulo_obst import EstimuloObst
from ecr.reaccao import Reaccao


class EvitarDir(Reaccao):
    """Classe que representa um comportamento de evitar uma direcao"""

    def __init__(self, direccao, resposta):
        """Construtor da classe"""
        estimulo = EstimuloObst(direccao)
        super().__init__(estimulo, resposta)
