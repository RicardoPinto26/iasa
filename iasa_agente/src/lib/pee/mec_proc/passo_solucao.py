from dataclasses import dataclass

from mod.estado import Estado
from mod.operador import Operador


@dataclass
class PassoSolucao:
    """Classe que representa um passo da solucao de um problema.
       Tem o estado atual, e o operador a aplicar sobre esse estado, para passar ao passo seguinte.
    """
    estado: Estado
    operador: Operador
