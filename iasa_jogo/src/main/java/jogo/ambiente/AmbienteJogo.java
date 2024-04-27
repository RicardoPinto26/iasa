package jogo.ambiente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*
    Classe que representa o ambiente do jogo.
    Trata-se de um ambiente virtual.
 */
public class AmbienteJogo implements Ambiente {
    /*
        Mapa de eventos possiveis dentro do jogo.
        Esta relação trata-se de uma composição, o que indica que a referencia so existe dentro do contexto
        do AmbienteJogo. Ou seja, os eventos só existem no contexto do AmbienteJogo.
     */
    private final Map<String, EventoJogo> eventos;
    /*
        Evento atual.
     */
    private EventoJogo evento;

    /*
        Scanner para leitura do input do utilizador.
     */
    private final Scanner scanner = new Scanner(System.in);

    /*
        Método que retorna o evento atual.
     */
    public EventoJogo getEvento() {
        return evento;
    }

    /*
        Contrutor do AmbienteJogo.
        Este inicia o mapa do eventos possiveis com a associação do input do utilizador com um evento.
     */
    public AmbienteJogo() {
        eventos = new HashMap<>();
        eventos.put("s", EventoJogo.SILENCIO);
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("o", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);
    }

    /*
        Método que evolui o ambiente.
        Neste caso, trata-se de gerar um novo evento, e atualizar o evento atual.
     */
    public void evoluir() {
        evento = gerarEvento();
    }

    /*
        Método que observa o ambiente.
        Neste caso, mostra o evento e retorna o evento atual.
     */
    public Evento observar() {
        evento.mostrar();
        return evento;
    }

    /*
        Método que executa um comando sobre o ambiente.
        Neste caso, apenas mostra o comando.
     */
    public void executar(Comando comando) {
        comando.mostrar();
    }

    /*
        Método que gera um evento.
        No contexto deste jogo, gerar um evento implica pedir ao utilizador por um evento.
     */
    private EventoJogo gerarEvento() {
        System.out.print("Evento?\n> ");
        String input = scanner.next();
        return eventos.get(input);
    }
}
