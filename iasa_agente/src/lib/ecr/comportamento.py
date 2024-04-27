from abc import ABC, abstractmethod


class Comportamento(ABC):
    """Classe abstrata que representa um comportamento, """

    @abstractmethod
    def activar(self, percepcao):
        """Activa o comportamento, retornando a accao que corresponde a percepcao"""
