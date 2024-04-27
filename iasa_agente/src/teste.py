from agente.agente_reactivo import AgenteReactivo as Agente
from sae import Simulador

# Executar simulador da SAE
Simulador(1, Agente()).executar()
