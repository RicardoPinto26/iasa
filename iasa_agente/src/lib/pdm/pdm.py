from pdm.mec_util import MecUtil


class PDM:
    def __init__(self, modelo, gama, delta_max):
        """Constructor da classe."""
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)

    def politica(self, U):
        """
        Calcula a politica para cada estado do modelo.
        Uma politica é um mapa de estado para accao, sendo a accao a que tem maior utilidade.
        A politica e calculada da seguinte forma:
        s = estado
        a = accao
        sn = estado sucessor de s, dada a accao a
        T = probabilidade de transicao do estado s para o estado sn, dado a accao a
        R = recompensa de transicao do estado s para o estado sn, dado a accao a
        y = taxa de desconto
        U = mapa de utilidades final
        U(s, a) = soma(T(s, a, sn) * (R(s, a, sn) + y * U(sn)), para cada sn)
        pol(s) = argmax(a, U(s, a))
        """
        politica = {}
        for s in self.__modelo.S():
            accoes = self.__modelo.A(s)
            if accoes:
                politica[s] = max(accoes, key=lambda a: self.__mec_util.util_accao(s, a, U))
        return politica

    def resolver(self):
        """Calcula a utilidade e a politica para o modelo, de modo a poder resolver o problema de decisao de Markov."""
        utilidade = self.__mec_util.utilidade()
        return utilidade, self.politica(utilidade)
