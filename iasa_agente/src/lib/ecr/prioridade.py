from .comport_comp import ComportamentoComp


class Prioridade(ComportamentoComp):
    """Comportamento composto em que as accoes são seleccionadas de acordo com uma prioridade associada
       que varia ao longo da execuccao.
    """

    def seleccionar_accao(self, accoes):
        """Seleciona uma accao de acordo com a sua prioridade"""
        if accoes:
            return max(accoes, key=lambda accao: accao.prioridade)
