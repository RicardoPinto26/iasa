from mod.estado import Estado


class EstadoAmbiente1D(Estado):
    """Classe que representa um estado do ambiente 1D."""

    def __init__(self, coordenada, terminal=False):
        """Construtor da classe. Guarda a sua coordenada."""
        self.coordenada = coordenada
        self.terminal = terminal

    def id_valor(self):
        """Identificador de um estado é a sua coordenada no ambiente"""
        return self.coordenada
