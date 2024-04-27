from agente.controlo_react.controlo_react import ControloReact
from agente.controlo_react.reaccoes.recolher import Recolher
from sae import Agente


class AgenteReactivo(Agente):
    """Classe que representa um Agente Reactivo.
    Neste tipo de agente o comportamento do sistema e gerado de forma reactiva,
    com base em associacoes entre estimulos (referentes as percepcoes) e respostas (referentes as accoes).
    """

    def __init__(self):
        """Contructor da classe.
        Utiliza o comportamento Recolher e um controlo reactivo.
        """
        comportamento = Recolher()
        controlo = ControloReact(comportamento)
        super().__init__(controlo)
