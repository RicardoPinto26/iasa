from pee.mec_proc.mecanismo_procura import MecanismoProcura


class ProcuraGrafo(MecanismoProcura):
    """Classe que implementa o mecanismo de procura, para procura em grafo."""

    def _iniciar_memoria(self):
        """Inicia a memoria, iniciando tambem os explorados com um dicionario vazio."""
        super()._iniciar_memoria()

        # Explorados é um dicionario Estado -> No
        self._explorados = {}

    def _memorizar(self, no):
        """Memoriza um no, adicionando-o a lista de explorados."""
        if self._manter(no):
            self._explorados[no.estado] = no
            self._fronteira.inserir(no)

    def _manter(self, no):
        """Verifica se um no deve ser mantido nos explorados."""

        # Se o estado do no nao estiver nas chaves do dicionario de explorados, retorna True,
        # caso contrario, retorna False.
        return no.estado not in self._explorados
