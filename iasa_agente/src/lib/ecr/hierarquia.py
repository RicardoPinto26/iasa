from .comport_comp import ComportamentoComp


class Hierarquia(ComportamentoComp):
    """Comportamento composto em que os comportamentos estao organizados numa hierarquia fixa
       de subsuncao (supressao e substituicao)
    """

    def seleccionar_accao(self, accoes):
        """Seleciona uma accao de acordo com a sua posicao hierarquica"""
        if accoes:
            return accoes[0]
