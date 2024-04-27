from abc import ABC, abstractmethod

from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao


class MecanismoProcura(ABC):
    """Classe que representa um mecanismo de procura.
       Permite procurar uma solucao para um problema.
       Utiliza um fronteira de exploracao para memorizar e gerir os nos explorados.
    """

    def __init__(self, fronteira):
        """Construtor da classe"""
        self._fronteira = fronteira

    def _iniciar_memoria(self):
        """Inicia estruturas de memoria de procura de acordo com o tipo de procura,
           incluindo a fronteira de exploracao.
           Como este mecanismo de procura e generico, apenas inicia a fronteira.
           """
        self._fronteira.iniciar()

    @abstractmethod
    def _memorizar(self, no):
        """Memoriza um no, genericamente."""

    def procurar(self, problema):
        """Procura uma solucao para um problema, usando o mecanismo de procura, de forma generica.
           Retorna a solucao encontrada ou None.
           """
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)
        while not self._fronteira.vazia:
            no = self._fronteira.remover()
            if problema.objectivo(no.estado):
                return Solucao(no)
            for no in self._expandir(problema, no):
                self._memorizar(no)

    def _expandir(self, problema, no):
        """Expande um no, gerando os seus nos sucessores."""
        sucessores = []
        estado = no.estado

        for operador in problema.operadores:
            estado_sucessor = operador.aplicar(estado)
            if estado_sucessor is not None:
                custo = no.custo + operador.custo(estado, estado_sucessor)
                no_sucessor = No(estado_sucessor, operador, no, custo)
                sucessores.append(no_sucessor)
        return sucessores
