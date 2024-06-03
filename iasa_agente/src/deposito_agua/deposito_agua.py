from mod_prob.problema_deposito import ProblemaDeposito
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif

VALOR_INICIAL = 0
VALOR_FINAL = 9

problema = ProblemaDeposito(VALOR_INICIAL, VALOR_FINAL)

mec_proc = ProcuraCustoUnif()
solucao = mec_proc.procurar(problema)

if solucao:
    print("Solução encontrada:")
    for passo in solucao:
        print(passo.estado.volume, passo.operador.volume_transferido)
else:
    print("Solução não encontrada")
