from abc import ABC, abstractmethod


class Fronteira(ABC):
    """Classe que representa uma fronteira de exploracao.
       Uma fronteira de exploracao e uma estrutura de dados que contem os nos a explorar."""

    @property
    def vazia(self):
        """Indica se a fronteira esta vazia.
           É uma propriedade derivada, ou seja, e calculada em tempo de execucao, e nao tem um
           backing field.
        """
        return self._nos == []

    @property
    def dimensao(self):
        """Retorna a dimensao da lista de nos"""
        return len(self._nos)

    def __init__(self):
        """Construtor da classe"""
        self.iniciar()

    def iniciar(self):
        """Inicia a fronteira, criando a estrutura de dados que vai conter os nos"""
        self._nos = []

    @abstractmethod
    def inserir(self, no):
        """Insere um no na fronteira."""

    def remover(self):
        """Remove o primeiro no da fronteira e retorna-o."""
        if not self.vazia:
            return self._nos.pop(0)
