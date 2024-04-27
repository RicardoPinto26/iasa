class Resposta:
    """Classe que representa uma resposta a uma estimulo, em termos de acção a realizar e
        da respectiva prioridade
    """

    def __init__(self, accao):
        """Contrutor da classe Resposta"""
        self._accao = accao

    def activar(self, percepcao, intensidade=0.0):
        """Activa a resposta, que no caso geral apenas define a prioridade da accao igual a intensidade
            e retorna a accao associada a resposta.

            Recebe a percepcao para garantir restricoes de activacao, se necessario.
        """
        self._accao.prioridade = intensidade
        return self._accao
