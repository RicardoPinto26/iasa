from random import choice

from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae import Direccao


class RespostaEvitar(RespostaMover):
    """Classe que representa a resposta de mover para evitar um obstaculo."""

    def __init__(self, dir_inicial=Direccao.ESTE):
        """Construtor da classe"""
        self.__direccoes = list(Direccao)

        super().__init__(dir_inicial)

    def activar(self, percepcao, intensidade=0.0):
        if percepcao.contacto_obst(self._accao.direccao):
            direccao = self.__direccao_livre(percepcao)
            if direccao is None:
                return None
            self._accao.direccao = direccao
        return super().activar(percepcao, intensidade)

    def __direccao_livre(self, percepcao):
        """Escolhe uma direccao para onde o agente se pode mover sem colidir com um obstaculo.
        """
        # Mudanca para escolha aleatoria de direccao
        dir_livres = [direccao for direccao in self.__direccoes if not percepcao.contacto_obst(direccao)]
        if dir_livres:
            return choice(dir_livres)
        return None
