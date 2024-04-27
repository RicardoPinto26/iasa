from abc import ABC, abstractmethod


class Operador(ABC):
    """Classe que representa um operador num problema de planeamento.
       Os operadores representam accoes que produzem a mudança de estado.
       Operam sobre as representacoes internas de estado, produzindo transicoes
       de estado que correspondem a geracao de novos estados.
    """

    @abstractmethod
    def aplicar(self, estado):
        """Aplica o operador sobre um estado, retornando o estado resultante."""

    @abstractmethod
    def custo(self, estado, estado_suc):
        """Devolve o custo de transicao do estado para o estado_suc, usando o operador."""
