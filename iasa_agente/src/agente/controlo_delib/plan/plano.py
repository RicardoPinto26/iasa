from abc import ABC, abstractmethod


class Plano(ABC):
    """Representa um plano de accoes."""
    @abstractmethod
    def obter_accao(self, estado):
        """Obtem a accao correspondente ao estado dado."""

    @abstractmethod
    def mostrar(self, vista):
        """Mostra na vista a informacao sobre o plano"""
