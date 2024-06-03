from mod_prob.estado_deposito import EstadoDeposito
from mod_prob.operador_transferir import OperadorTransferir


class OperadorEncher(OperadorTransferir):
    """Operador enche o deposito com a capacidade do recepiente"""

    def aplicar(self, estado):
        return EstadoDeposito(estado.volume + self.volume_transferido)
