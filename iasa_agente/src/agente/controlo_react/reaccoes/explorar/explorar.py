from random import choice

from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.comportamento import Comportamento
from sae import Direccao


def _direccao_aleatoria():
    """Funcao que escolhe e retorna uma direccao aleatoriamente,
    atraves da funcao choice do modulo random.
    """
    return choice(list(Direccao))


class Explorar(Comportamento):
    """Classe que representa um comportamento de explorar."""

    def activar(self, percepcao):
        """Metodo que activa o comportamento com uma percepcao
        Escolhe uma direccao aleatoriamente, usando a funcao _direccao_aleatoria.
        Cria uma resposta de mover com a direccao escolhida, activa-a e retorna a accao devolvida.
        """
        direccao = _direccao_aleatoria()
        resposta = RespostaMover(direccao)
        return resposta.activar(percepcao)
