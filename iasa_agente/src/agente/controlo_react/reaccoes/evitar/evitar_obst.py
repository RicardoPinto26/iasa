from agente.controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from agente.controlo_react.reaccoes.evitar.resposta_evitar import RespostaEvitar
from ecr.hierarquia import Hierarquia
from sae import Direccao


class EvitarObst(Hierarquia):
    """Classe que representa um comportamento de evitar um obstaculo.
       Utiliza o mecanismo de selecao de accao por hierarquia.
    """

    def __init__(self):
        """Construtor da classe"""
        self.__resposta = RespostaEvitar()
        comportamentos = [EvitarDir(direccao, self.__resposta) for direccao in Direccao]
        super().__init__(comportamentos)
