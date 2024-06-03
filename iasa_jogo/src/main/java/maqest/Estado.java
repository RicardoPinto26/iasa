package maqest;

import agente.Accao;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;

/*
    Classe que representa um estado da maquina de estados.
    Um estado representa a situacao de evolucao de um sistema.

    As transicoes sao ditadas por eventos, sendo que os eventos tem uma transicao associada.
 */
public class Estado {
    /*
        Nome do estado.
     */
    private String nome;
    /*
        Mapa de Evento -> Transicao.
        Representa as transicoes possiveis a partir deste estado.
     */
    private Map<Evento, Transicao> transicoes;

    public Estado(String nome) {
        this.nome = nome;

        transicoes = new HashMap<>();
    }

    public String getNome() {
        return nome;
    }

    /*
        Neste caso, processar significa retornar a transicao associada ao evento, ou null caso nao exista.
     */
    Transicao processar(Evento evento) {
        return transicoes.get(evento);
    }

    /*
        Metodo que adiciona uma transicao ao mapa de evento -> transicao, sem accao associada.
        Return this para permitir a chamada a varios metodos da classe em sequencia.
     */
    public Estado transicao(Evento evento, Estado estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }

    /*
        Metodo que adiciona uma transicao ao mapa de evento -> transicao.
        Return this para permitir a chamada a varios metodos da classe em sequencia.
     */
    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao) {
        Transicao transicao = new Transicao(estadoSucessor, accao);
        transicoes.put(evento, transicao);
        return this;
    }
}
