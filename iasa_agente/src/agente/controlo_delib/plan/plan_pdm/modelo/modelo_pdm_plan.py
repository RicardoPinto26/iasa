from agente.controlo_delib.modelo.modelo_plan import ModeloPlan
from pdm.modelo_pdm import ModeloPDM


class ModeloPDMPlan(ModeloPlan, ModeloPDM):
    """Modelo de planeamento baseado no processo de decisao de Markov.
       Implementa as interfaces ModeloPlan e ModeloPDM, desta forma, pode encapsular um modelo de planeamento, de modo
       a ser utilizado pelo agente nas outras operacoes, e ser tambem utilizado no processo de decisao de Markov"""

    def __init__(self, modelo_plan, objectivos, rmax=1000):
        """Construtor da classe."""
        self.__modelo_plan = modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax

        # Cria um mapa (estado, accao) -> estado, com todas as transicoes possiveis
        self.__transicoes = {
            (s, a): a.aplicar(s)
            for s in self.obter_estados()
            for a in self.obter_operadores()
        }

    def obter_estado(self):
        """Retorna o estado atual, delegando esta tarefa para o modelo de planeamento."""
        return self.__modelo_plan.obter_estado()

    def obter_estados(self):
        """Retorna os estados do modelo, delegando esta tarefa para o modelo de planeamento."""
        return self.__modelo_plan.obter_estados()

    def obter_operadores(self):
        """Retorna todos os operadores do modelo, delegando esta tarefa para o modelo de planeamento."""
        return self.__modelo_plan.obter_operadores()

    def S(self):
        """Retorna todos os estados"""
        return self.obter_estados()

    def A(self, s):
        """Retorna todos os operadores, exceto se o estado for um objectivo."""
        return self.obter_operadores() if s not in self.__objectivos else []

    def T(self, s, a, sn):
        """Como e deterministico, a probabilidade de transicao e sempre 1, se a transicao for possivel."""
        return 1 if self.__transicoes.get((s, a)) == sn else 0

    def R(self, s, a, sn):
        """O custo de transicao e igual ao custo da accao,
        ou se o estado sucessor for um objectivo, o valor maximo de recompensa."""
        return self.__rmax if sn in self.__objectivos else -a.custo(s, sn)

    def suc(self, s, a):
        """Como e deterministico, apenas um estado sucessor existe.
        Caso o estado sucessor nao exista, retorna uma lista vazia."""
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else []
