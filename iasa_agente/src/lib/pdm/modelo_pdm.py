from abc import ABC, abstractmethod


class ModeloPDM(ABC):
    """
    Classe abstrata que define o modelo de um processo de decisao de Markov.
    Este modelo deve ser capaz de retornar:
    - Os estados do modelo.
    - As accoes possiveis para um determinado estado.
    - A probabilidade de transicao de um estado para outro, dado uma accao.
    - A recompensa de transicao de um estado para outro, dado uma accao.
    - Os estados sucessores para um estado, dado uma accao.
    """

    @abstractmethod
    def S(self):
        """
        Retorna a lista de estados do modelo.
        """

    @abstractmethod
    def A(self, s):
        """
        Retorna a lista de acoes possiveis para o estado s.
        """

    @abstractmethod
    def T(self, s, a, sn):
        """
        Retorna a probabilidade de transicao do estado s para o estado sn, dado a accao a.
        """

    @abstractmethod
    def R(self, s, a, sn):
        """
        Retorna a recompensa de transicao do estado s para o estado sn, dado a accao a.
        """

    @abstractmethod
    def suc(self, s, a):
        """
        Retorna a lista de estados sucessores possiveis para s, dado a accao a.
        """
