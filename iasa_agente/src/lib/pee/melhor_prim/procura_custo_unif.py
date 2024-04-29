from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim


class ProcuraCustoUnif(ProcuraMelhorPrim):
    """Classe que implementa o mecanismo de procura melhor primeiro, para procura de custo uniforme.
       A procura de custo uniforme é uma procura de melhor primeiro, em que o no a expandir, ou seja,
        o primeiro no da fronteira, e o no com menor custo acumulado.
    """
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())
