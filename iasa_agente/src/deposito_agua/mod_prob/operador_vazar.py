from mod_prob.estado_deposito import EstadoDeposito
from mod_prob.operador_transferir import OperadorTransferir


class OperadorVazar(OperadorTransferir):
    """Operador que vazia o deposito com a capacidade do recepiente"""

    def aplicar(self, estado):
        """Aplica o operador ao estado, retornando o estado com o volume resultante.
        Caso o volume a vazar seja superior ao volume do deposito, o volume resultante e 0"""
        return EstadoDeposito(max(0, estado.volume - self.volume_transferido))
