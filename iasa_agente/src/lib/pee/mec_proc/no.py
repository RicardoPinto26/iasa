class No:
    """Classe que representa um no da arvore de procura."""

    @property
    def profundidade(self):
        """Representa a profundidade do no na arvore de procura."""
        return self.__profundidade

    @property
    def custo(self):
        """Representa o custo do caminho da raiz ate este no."""
        if self.__custo is not None:
            return self.__custo
        return 0

    @property
    def estado(self):
        """Representa o estado do no."""
        return self.__estado

    @property
    def operador(self):
        """Representa o operador que foi aplicado para chegar a este no."""
        return self.__operador

    @property
    def antecessor(self):
        """Representa o no antecessor deste no."""
        return self.__antecessor

    def __init__(self, estado, operador=None, antecessor=None, custo=0):
        """Construtor da classe"""
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo

        if self.__antecessor is None:
            self.__profundidade = 0
        else:
            self.__profundidade = self.__antecessor.profundidade + 1

    def __lt__(self, other):
        """Metodo less-than, para comparar dois nos.
           Necessario para a comparacao de tuplos na fronteira de prioridade"""
        return self.custo < other.custo
