from agente.controlo_react.reaccoes.aproximar.estimulo_alvo import EstimuloAlvo
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao


class AproximarDir(Reaccao):
    """Classe que representa um comportamento de aproximação numa direcao"""

    def __init__(self, direccao):
        """Construtor da classe"""
        estimulo = EstimuloAlvo(direccao)
        resposta = RespostaMover(direccao)
        super().__init__(estimulo, resposta)
