package maqest;

import agente.Accao;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;

/*
    Classe que representa um estado da máquina de estados.
    Um estado representa a situação de evolução de um sistema.

    As transicoes são ditadas por eventos, sendo que os eventos têm uma transicao associada.
 */
public class Estado {
    private  String nome;
    private Map<Evento, Transicao> transicoes;

    public String getNome() {
        return nome;
    }

    public Estado(String nome) {
        this.nome = nome;

        transicoes = new HashMap<>();
    }

    /*
        Neste caso, processar significa retornar a transicao associada ao evento, ou null caso não exista.
     */
    Transicao processar(Evento evento) {
        return transicoes.get(evento);
    }

    public Estado transicao(Evento evento, Estado estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }

    /*
        Método que adiciona uma transição ao mapa de evento -> transicao.
        Return this para permitir a chamada a vários métodos da classe em sequencia.
     */
    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao) {
        Transicao transicao = new Transicao(estadoSucessor, accao);
        transicoes.put(evento, transicao);
        return this;
    }
}
