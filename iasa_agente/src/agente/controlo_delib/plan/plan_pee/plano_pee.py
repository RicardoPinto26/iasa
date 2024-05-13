from agente.controlo_delib.plan.plano import Plano


class PlanoPEE(Plano):
    """Representa um plano de accoes gerado por um planeador de procura em espaco de estados.
    """
    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao]

    def obter_accao(self, estado):
        """Obtem a accao a executar para o estado dado.
           Caso o estado nao seja o proximo estado na sequencia de passos, retorna None, visto que o plano
           ja nao e valido."""
        if not self.__passos:
            return None

        passo = self.__passos.pop(0)
        if passo.estado == estado:
            return passo.operador

    def mostrar(self, vista):
        """Mostra na vista a informacao sobre os passos do plano, produzindo na vista uma serie de vetores,
           que indicam a direcao que o agente segue em cada passo."""
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)
