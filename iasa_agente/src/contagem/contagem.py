from mod_prob.heuristica_contagem import HeuristicaContagem
from mod_prob.problema_contagem import ProblemaContagem

# from pee.larg.procura_largura import ProcuraLargura as Procura
# from pee.prof.procura_profundidade import ProcuraProfundidade as Procura
# from pee.prof.procura_prof_lim import ProcuraProfLim as Procura
# from pee.prof.procura_prof_iter import ProcuraProfIter as Procura
# from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif as Procura
from pee.melhor_prim.procura_sofrega import ProcuraSofrega as Procura
# from pee.melhor_prim.procura_aa import ProcuraAA as Procura


VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2, -1]

problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)

mec_proc = Procura()

# solucao = mec_proc.procurar(problema)
heuristica = HeuristicaContagem(VALOR_FINAL)
solucao = mec_proc.procurar(problema, heuristica)

if solucao:
    print("Solução encontrada:")
    for passo in solucao:
        print(passo.estado.valor, passo.operador.incremento)
else:
    print("Solução não encontrada")
