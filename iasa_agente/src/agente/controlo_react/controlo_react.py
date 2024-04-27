from sae import Controlo


class ControloReact(Controlo):
    """Classe que representa um controlo reactivo"""

    def __init__(self, comportamento):
        """Construtor da classe ControloReact"""
        self.__comportamento = comportamento
        self.mostrar_per_dir = True  # Mostrar a informacao sensorial

    def processar(self, percepcao):
        """Processa a percepcao, activando o comportamento interno"""
        return self.__comportamento.activar(percepcao)
