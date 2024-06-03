from agente.controlo_delib.plan.plano import Plano


class PlanoPDM(Plano):
    """Representa um plano de accoes gerado por um planeador baseado no processo de decisao de Markov."""
    def __init__(self, utilidade, politica):
        """Construtor da classe."""
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        """Retorna a accao associada ao estado, conforme a politica"""
        if self.__politica:
            return self.__politica.get(estado)

    def mostrar(self, vista):
        """Mostra a informacao sobre a politica e utilidades do plano."""
        if self.__politica:
            for estado, valor in self.__utilidade.items():
                # Mostra a utilidade de cada estado
                vista.mostrar_valor_posicao(estado.posicao, valor)
            for estado, accao in self.__politica.items():
                # mostra a politica (ou seja, a accao a aplicar em cada estado)
                vista.mostrar_vector(estado.posicao, accao.ang)
