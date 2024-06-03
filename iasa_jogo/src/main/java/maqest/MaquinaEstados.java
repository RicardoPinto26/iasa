package maqest;

import agente.Accao;
import ambiente.Evento;

/*
    Classe que representa uma máquina de estados.
 */
public class MaquinaEstados {
    private Estado estado;

    public MaquinaEstados(Estado estadoInicial) {
        estado = estadoInicial;
    }

    public Estado getEstado() {
        return estado;
    }

    /*
        Metodo que representa o processamento de um evento na maquina de estados.
        Caso o evento nao represente uma transicao no estado atual, retorna null, caso contrario, muda
        o estado atual para o estado sucessor da transicao, e retorna a accao correspondente a transicao.
     */
    public Accao processar(Evento evento) {
        Transicao transicao = estado.processar(evento);
        if (transicao != null) {
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        } else {
            return null;
        }
    }
}
