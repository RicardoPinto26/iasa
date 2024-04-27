from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.comportamento import Comportamento
from sae import Direccao


class ContarPassos(Comportamento):
    """Classe que representa um comportamento de contar passos.
       Este é um comportamento de uma arquitetura reactiva com memória.
       Numa arquitetura deste tipo, as reaccoes dependem nao so das percepcoes, mas tambem da memoria de
       percepcoes anteriores (ou de informacao delas derivada) para gerar as accoes. Neste caso, nem sequer
       depende das percepcoes, apenas do numero de passos que o agente deu (memoria).
    """

    def __init__(self):
        """Construtor da classe que inicializa o contador de passos e a resposta de mover para norte."""
        self.__contador = 0  # Contador de passos, e a memoria interna do comportamento
        self.__resposta = RespostaMover(Direccao.NORTE)

    def activar(self, percepcao):
        """Metodo que activa o comportamento, independente da percepcao.
        Conta o numero de passos, e se for igual ou superior a 10, retorna uma resposta de mover para norte
        """
        self.__contador += 1
        print(self.__contador)
        if self.__contador >= 10:
            return self.__resposta.activar(percepcao)
