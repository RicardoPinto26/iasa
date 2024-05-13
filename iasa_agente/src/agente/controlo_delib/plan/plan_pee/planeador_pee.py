from agente.controlo_delib.plan.plan_pee.mod_prob.heur_dist import HeurDist
from agente.controlo_delib.plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from agente.controlo_delib.plan.plan_pee.plano_pee import PlanoPEE
from agente.controlo_delib.plan.planeador import Planeador
from pee.melhor_prim.procura_aa import ProcuraAA


class PlaneadorPEE(Planeador):
    """Representa um planeador baseado em procura em espaco de estados.
       Utiliza um mecanismo de procura melhor primeiro, para que possam ser usadas ambas
       a procura sofrega e a procura A*.
       """

    def __init__(self):
        # Neste caso, utilizamos a procura A*.
        self.__mec_pee = ProcuraAA()

    def planear(self, modelo_plan, objectivos):
        """Planeia um plano para atingir um estado_final.
           Neste caso, os objectivos recebidos estao ordenados por distancia ao agente, e como tal
           o estado_final escolhido e o objectivo com menor distancia (ou seja, o primeiro da lista)."""
        if not objectivos:
            return None

        estado_final = objectivos[0]
        problema = ProblemaPlan(modelo_plan, estado_final)
        heuristica = HeurDist(estado_final)
        solucao = self.__mec_pee.procurar(problema, heuristica)

        if solucao:
            return PlanoPEE(solucao)
