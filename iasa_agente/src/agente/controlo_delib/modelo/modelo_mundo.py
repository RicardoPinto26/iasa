import math

from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from agente.controlo_delib.modelo.modelo_plan import ModeloPlan
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from sae import Direccao
from sae import Elemento


class ModeloMundo(ModeloPlan):
    """Classe que representa o modelo do mundo.
       O modelo do mundo e a representacao interna do ambiente, e serve como suporte para o
       raciocinio automatico do agente deliberativo.
       E atualizado com base nas percepcoes do agente.
    """

    @property
    def alterado(self):
        """Indica se o modelo foi alterado na ultima atualizacao."""
        return self.__alterado

    @property
    def elementos(self):
        """Mapa de posicao -> Elemento, ou seja, cada entrada corresponde a um elemento do ambiente, onde
           chave dessa entrada e a sua posicao"""
        return self.__elementos

    def __init__(self):
        self.__alterado = False
        self.__estado = None
        self.__estados = None
        self.__elementos = None
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]

    def obter_estado(self):
        """Obtem o estado atual do modelo do mundo."""
        return self.__estado

    def obter_estados(self):
        """Obtem todos os estados do modelo do mundo, ou seja, tudo o que o agente sabe sobre o ambiente."""
        return self.__estados

    def obter_operadores(self):
        """Obtem os operadores possiveis."""
        return self.__operadores

    def obter_elemento(self, estado):
        """Obtem o elemento na posicao dada. Se nao existir, devolve None."""
        return self.__elementos.get(estado.posicao)

    def distancia(self, estado):
        """Devolve a distancia do agente ao estado dado."""
        return math.dist(self.__estado.posicao, estado.posicao)

    def actualizar(self, percepcao):
        self.__estado = EstadoAgente(percepcao.posicao)
        self.__estados = [EstadoAgente(pos) for pos in percepcao.posicoes]
        self.__elementos = percepcao.elementos
        self.__alterado = percepcao.recolha

    def mostrar(self, vista):
        """Mostra a informacao do modelo do mundo.
           Para cada Alvo e Obstaculo no mapa de elementos, mostra-o na vista.
           Marca tambem a posicao do agente na vista"""
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)
