package maqest;

import agente.Accao;
import ambiente.Evento;

/*
    Classe que representa uma máquina de estados.
 */
public class MaquinaEstados {
    private Estado estado;

    public Estado getEstado() {
        return estado;
    }

    public MaquinaEstados(Estado estadoInicial) {
        estado = estadoInicial;
    }

    /*
        Método que representa o processamento de um evento na máquina de estados.
        Caso o evento não represente uma transicao no estado atual, retorna null, caso contrario, muda
        o estado atual para o estado sucessor da transicao, e retorna a accao correspondente à transicao.
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
