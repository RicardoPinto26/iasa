from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade
from sae import Direccao


class AproximarAlvo(Prioridade):
    """Classe que representa um comportamento de aproximacao de um alvo.
       Utiliza o mecanismo de selecao de accao por prioridade.
    """

    def __init__(self):
        """Construtor da classe que cria a lista de comportamentos para cada direcao"""
        comportamentos = [AproximarDir(direccao) for direccao in Direccao]  # Usa uma list comprehension
        super().__init__(comportamentos)
