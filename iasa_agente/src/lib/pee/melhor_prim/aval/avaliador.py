from abc import abstractmethod, ABC


class Avaliador(ABC):
    """Classe abstrata que define a interface de um avaliador de nos"""
    @abstractmethod
    def prioridade(self, no):
        """Devolve a prioridade do no"""
