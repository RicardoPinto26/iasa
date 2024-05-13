class MecUtil:
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max

    def utilidade(self):
        raise NotImplementedError

    def util_accao(self, s, a, U):
        raise NotImplementedError