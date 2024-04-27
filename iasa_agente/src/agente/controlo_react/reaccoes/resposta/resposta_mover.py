from ecr.resposta import Resposta
from sae import Accao


class RespostaMover(Resposta):
    """Classe que representa uma resposta de mover."""

    def __init__(self, direccao):
        """Construtor da classe. Recebe uma direccao, e cria a accao correspondente com a direccao.
        Passa para o construtor da superclasse a accao criada.
        """
        accao = Accao(direccao)
        super().__init__(accao)
