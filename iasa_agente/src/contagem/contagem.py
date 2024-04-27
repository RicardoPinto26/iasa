from mod_prob.problema_contagem import ProblemaContagem

# from pee.prof.procura_profundidade import ProcuraProfundidade as Procura
# from pee.prof.procura_prof_lim import ProcuraProfLim as Procura
from pee.prof.procura_prof_iter import ProcuraProfIter as Procura
# from pee.larg.procura_largura import ProcuraLargura as Procura

VALOR_INICIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1, 2, -1]

problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)

mec_proc = Procura()

solucao = mec_proc.procurar(problema)

if solucao:
    print("Solução encontrada:")
    for passo in solucao:
        print(passo.estado.valor, passo.operador.incremento)
else:
    print("Solução não encontrada")
