from sae import Elemento


class MecDelib:
    """Classe que implementa um mecanismo de deliberacao."""
    def __init__(self, modelo_mundo):
        """Construtor da classe"""
        self.__modelo_mundo = modelo_mundo

    def deliberar(self):
        """Delibera o que fazer, ou seja, gerar um conjunto de objectivos.
           Neste caso, gera um conjunto de estados objectivo, que são os estados cuja
           posicao contém um alvo.
        """
        estados = self.__modelo_mundo.obter_estados()
        objectivos = [estado for estado in estados
                      if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]

        if objectivos:
            # Ordena os objectivos por ordem crescente de distancia ao agente
            objectivos.sort(key=self.__modelo_mundo.distancia)
            return objectivos
