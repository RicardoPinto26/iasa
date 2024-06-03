# from agente.agente_reactivo import AgenteReactivo as Agente
from agente.agente_delib_pee import AgenteDelibPEE as Agente
# from agente.agente_delib_pdm import AgenteDelibPDM as Agente
from sae import Simulador

# Executar simulador da SAE
Simulador(4, Agente()).executar()
