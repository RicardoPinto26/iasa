from agente.controlo_delib.mec_delib import MecDelib
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from sae import Controlo


class ControloDelib(Controlo):
    """Classe que representa um controlo deliberativo.
       O controlo deliberativo engloba o processamento interno do agente deliberativo, incluindo:
       - Modelo do mundo
       - Mecanismo de deliberacao
       - Planeador
    """

    def __init__(self, planeador):
        """Construtor da classe"""
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__planeador = planeador
        self.__objectivos = None
        self.__plano = None

    def processar(self, percepcao):
        """Processo de tomada de decisao e accao:
        1. Atualizar o modelo do mundo, com a percepcao, neste caso, assimilar
        Se for necessario reconsiderar:
            2. Deliberar o que fazer, ou seja, gerar uma lista de objectivos
            3. Planear como fazer, neste caso, seguindo o planeador
        4. Executar o plano, ou seja, obter a accao a executar
        """
        self.__assimilar(percepcao)

        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()

        self.__mostrar()
        return self.__executar()

    def __assimilar(self, percepcao):
        """Assimila a percepcao, ou seja, atualiza o modelo do mundo com a percepcao."""
        self.__modelo_mundo.actualizar(percepcao)

    def __reconsiderar(self):
        """Verifica se é preciso reconsiderar, ou seja, deliberar e planear novamente.
           É necessário reconsiderar se nao existir um plano, ou se o modelo do mundo foi alterado.
        """
        return self.__plano is None or self.__modelo_mundo.alterado

    def __deliberar(self):
        """Delibera o que fazer, ou seja, gera uma lista de objectivos atraves do
        mecanismo de deliberacao."""
        self.__objectivos = self.__mec_delib.deliberar()

    def __planear(self):
        """Planeia como fazer, ou seja, gera um plano de accao atraves do planeador."""
        self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)

    def __executar(self):
        """Executa o plano se este existir."""
        if self.__plano:
            estado = self.__modelo_mundo.obter_estado()
            operador = self.__plano.obter_accao(estado)
            if operador:
                return operador.accao

            self.__plano = None

    def __mostrar(self):
        """Mostra informacao sobre o controlo deliberativo.
           Limpa a vista, mostra o modelo do mundo, o plano (se existir) e os objectivos (se existirem)."""
        self.vista.limpar()

        self.__modelo_mundo.mostrar(self.vista)

        if self.__plano:
            self.__plano.mostrar(self.vista)

        if self.__objectivos:
            for objectivo in self.__objectivos:
                self.vista.marcar_posicao(objectivo.posicao)
