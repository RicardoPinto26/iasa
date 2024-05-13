import math

from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from mod.operador import Operador
from sae.agente.accao import Accao


class OperadorMover(Operador):
    """Operador de mover"""
    @property
    def ang(self):
        return self.__accao.ang

    @property
    def accao(self):
        return self.__accao

    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__direccao = direccao
        self.__accao = Accao(direccao)

    def aplicar(self, estado):
        """Aplicar o operador sobre um estado.
           Para aplicar o operador, e necessario calcular a nova posicao do agente.
           Para o novo estado ser valido, este deve estar na lista de estados do modelo do mundo.
        """
        x, y = estado.posicao

        passo = self.__accao.passo
        ang = self.__accao.ang

        dx = round(passo * math.cos(ang))
        dy = round(-passo * math.sin(ang))

        novo_estado = EstadoAgente((x + dx, y + dy))
        if novo_estado in self.__modelo_mundo.obter_estados():
            return novo_estado

    def custo(self, estado, estado_suc):
        """Custo de mover é a distancia euclidiana entre a posicao do estado e do estado sucessor."""
        return math.dist(estado.posicao, estado_suc.posicao)
