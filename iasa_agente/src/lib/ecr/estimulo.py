from abc import ABC, abstractmethod


class Estimulo(ABC):
    """Classe abstrata que representa um estimulo, que define informacao activadora de uma reaccao"""

    @abstractmethod
    def detectar(self, percepcao):
        """Detecta a intensidade de uma percepcao"""
