from pee.melhor_prim.aval.avaliador_sof import AvaliadorSof
from pee.melhor_prim.procura_informada import ProcuraInformada


class ProcuraSofrega(ProcuraInformada):
    """Classe que representa uma procura sofrega.
       E completo mas nao optimo, ou seja, encontra sempre solucao, mas esta pode nao ser a de menor custo.
       Tem um custo computacional mais baixo, visto que nao tem em conta o custo de percurso ate ao no atual.
       Ao procurar, tem em conta a minimizacao da estimativa de custo (heuristica) ate ao objectivo.
    """

    def __init__(self):
        """Construtor da classe"""
        super().__init__(AvaliadorSof())
