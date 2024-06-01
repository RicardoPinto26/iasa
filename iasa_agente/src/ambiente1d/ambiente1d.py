from mod_prob.modelo_ambiente1d import ModeloAmbiente1DPDM
from pdm.pdm import PDM

modelo = ModeloAmbiente1DPDM()

gama = 0.5
delta_max = 0.0

pdm = PDM(modelo, gama, delta_max)

utilidade, politica = pdm.resolver()

print("U:", {s.coordenada: utilidade[s] for s in utilidade.keys()})
print("P:", {s.coordenada: '>' if politica[s].deslocamento == 1 else '<' for s in politica.keys()})
