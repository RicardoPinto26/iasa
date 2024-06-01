from mod_prob.estado_ambiente1d import EstadoAmbiente1D
from mod_prob.operador_mover import OperadorMover

from pdm.modelo_pdm import ModeloPDM


class ModeloAmbiente1DPDM(ModeloPDM):
    """Classe que representa o modelo do ambiente unidimensional 7x1.
       Existem 2 accoes possiveis, a de mover para a esquerda e a de mover para a direita.
       Os estados sao numerados de 1 a 7, sendo que o estado 1 e o estado 7 sao estados terminais.
       O estado 1 tem uma recompensa de -1 e o estado 7 tem uma recompensa de 1.
       Tentar mover para fora dos limites do ambiente nao tem efeito, ou seja,
       o agente permanece no mesmo estado. Funcionalmente, nao existem accoes possiveis nos estados terminais."""

    def __init__(self):
        coordenadas = range(1, 8)
        coord_min = coordenadas[0]
        coord_max = coordenadas[-1]
        self.__estados = [
            EstadoAmbiente1D(i, terminal=(i == coord_min or i == coord_max))
            for i in coordenadas
        ]
        self.__acoes = [
            OperadorMover(-1, coord_min, coord_max),
            OperadorMover(1, coord_min, coord_max)
        ]

    def S(self):
        return self.__estados

    def A(self, s):
        if s.terminal:
            return []
        return self.__acoes

    def T(self, s, a, sn):
        if s.terminal:
            return 0
        return 1

    def R(self, s, a, sn):
        if sn.coordenada == 1:
            return -1
        if sn.coordenada == 7:
            return 1
        return 0

    def suc(self, s, a):
        return [a.aplicar(s)]
