from mod_prob.estado_ambiente1d import EstadoAmbiente1D

from mod.operador import Operador


class OperadorMover(Operador):
    """Classe que representa um operador de mover no ambiente 1D."""

    def __init__(self, deslocamento, indice_minimo, indice_maximo):
        """Construtor da classe.
        Guarda o deslocamento a aplicar. O deslocamento representa
        o vector unidimensional (representado por um numero) de movimento do agente,
        ou seja, o numero de posicoes que o agente se desloca para a esquerda ou para a direita."""
        self.deslocamento = deslocamento
        self.__indice_minimo = indice_minimo
        self.__indice_maximo = indice_maximo

    def aplicar(self, estado):
        """Aplica o deslocamento ao estado e devolve o novo estado."""
        return EstadoAmbiente1D(
            min(max(self.__indice_minimo, estado.coordenada + self.deslocamento), self.__indice_maximo)
        )

    def custo(self, estado, estado_suc):
        return 0
