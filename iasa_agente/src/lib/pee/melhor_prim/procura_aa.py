from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA
from pee.melhor_prim.procura_informada import ProcuraInformada


class ProcuraAA(ProcuraInformada):
    """Classe que representa uma procura A*.
       E completo e optimo, ou seja, encontra sempre a solucao de menor custo.
       Tem um custo computacional menor do que a procura em profundidade, e e o melhor metodo de procura.
       Ao procurar, tem em conta a minimizacao da soma do custo de percurso ate ao no atual e
       da estimativa de custo (heuristica) ate ao objectivo.
    """

    def __init__(self):
        """Construtor da classe"""
        super().__init__(AvaliadorAA())
