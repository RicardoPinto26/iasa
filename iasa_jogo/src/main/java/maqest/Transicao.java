package maqest;

import agente.Accao;

/*
    Classe que representa uma transicao entre estados.
    Uma transicao é um acontecimento através do qual um sistema evolui para um novo estado.
 */
public class Transicao {
    private Estado estadoSucessor;
    private Accao accao;

    public Transicao(Estado estadoSucessor, Accao accao) {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }

    Estado getEstadoSucessor() {
        return estadoSucessor;
    }

    Accao getAccao() {
        return accao;
    }
}
