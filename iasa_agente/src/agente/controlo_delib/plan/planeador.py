from abc import ABC, abstractmethod


class Planeador(ABC):
    """Representa um planeador.
       Planeia planos de accao com base nos objectivos gerados pelo mecanismo de deliberacao."""
    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        """Gera os planos de accao"""
