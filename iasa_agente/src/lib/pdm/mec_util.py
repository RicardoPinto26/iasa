class MecUtil:
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max

    def utilidade(self):
        """
        Calcula a utilidade para cada estado do modelo.
        A utilidade e calculada da seguinte forma:
        s = estado
        a = accao
        U = mapa de utilidades anterior (na primeira iteracao, todos os valores sao 0)

        U = maximo(Uaccao(s, a, Uant), para cada accao possivel em s)
        """

        # Inicia o mapa de utilidades com a utilidade 0 para todos os estados
        U = {s: 0 for s in self.__modelo.S()}
        # Inicia o delta com um valor maior que o delta maximo, para que a primeira iteracao seja executada
        delta = self.__delta_max + 1

        # Enquanto o delta for maior que o delta maximo, atualiza as utilidades
        while delta > self.__delta_max:
            # Copia o mapa de utilidades, para manter uma copia do mapa antes da atualizacao
            U_ant = U.copy()
            # Inicia o delta atual a 0
            delta = 0
            # Para cada estado, calcula a utilidade maxima, e atualiza o delta atual para o valor maximo entre
            # o delta atual e o delta entre a utilidade atual e a utilidade anterior
            for s in self.__modelo.S():
                # Calcula a utilidade maxima para o estado s
                U[s] = max([self.util_accao(s, a, U) for a in self.__modelo.A(s)])
                # Atualiza o delta atual
                delta = max(delta, abs(U[s] - U_ant[s]))
        # Retorna o mapa de utilidades
        return U

    def util_accao(self, s, a, U):
        """
        Calcula a utilidade da accao sobre o estado s.
        A utilidade e calculada da seguinte forma:
        s = estado
        a = accao
        sn = estado sucessor de s, dado a accao a
        gama = factor de desconto
        U = mapa de utilidades atual

        Uaccao = soma(T(s, a, sn) * (R(s, a, sn) + gama * U[sn]), para cada sn)
        T = probabilidade de transicao do estado s para o estado sn, dado a accao a
        R = recompensa de transicao do estado s para o estado sn, dado a accao a
        """
        return sum([self.__modelo.T(s, a, sn) * (self.__modelo.R(s, a, sn) + self.__gama * U[sn])
                    for sn in self.__modelo.suc(s, a)])
