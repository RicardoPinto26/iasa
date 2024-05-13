from pee.mec_proc.passo_solucao import PassoSolucao


class Solucao:
    """Classe que representa um percurso correspondente a uma solucao de um problema.
    """

    @property
    def dimensao(self):
        """Representa a dimensao da solucao, ou seja, o numero de nos do percurso."""
        return self.__no_final.profundidade

    @property
    def custo(self):
        """Representa o custo total da solucao, ou seja, o custo do no final."""
        return self.__no_final.custo

    def __init__(self, no_final):
        """Construtor da classe.
           Gera a lista de passos da solucao."""

        # Troca por solucao com apenas um while, embora ambos os algoritmos sejam O(N),
        # sendo n o numero de nos. Esta solucao esta toda contida dentro do construtor.

        self.__no_final = no_final
        self.__passos = []

        no = self.__no_final
        while no.antecessor:
            self.__passos.insert(0, PassoSolucao(no.antecessor.estado, no.operador))
            no = no.antecessor

    def __iter__(self):
        """Retorna um iterador para a lista de passos da solucao."""
        return iter(self.__passos)

    def __getitem__(self, index):
        """Retorna o passo de indice index da solucao."""
        return self.__passos[index]
