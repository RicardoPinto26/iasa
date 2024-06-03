package jogo.ambiente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*
    Classe que representa o ambiente do jogo.
    Esta classe implementa a interface Ambiente, o que significa que tem de implementar os metodos definidos pelo contrato
    da interface Ambiente.

    Este ambiente trata-se de um ambiente com as seguintes propriedades:
    - Discreto
    - Deterministico
    - Dinamico
    - Totalmente observavel
    - Agente unico

    O ambiente do jogo é um ambiente de texto, onde os eventos que acontecem sao gerados pelo utilizador.

    Existe uma associacao para EventoJogo, atraves do atributo evento, mas existe tambem uma composicao para EventoJogo,
    atraves do atributo eventos.
    Existe tambem uma dependencia para Comando.
 */
public class AmbienteJogo implements Ambiente {
    /*
        Mapa de eventos possiveis dentro do jogo.
        Relaciona uma letra com um EventoJogo.
     */
    private final Map<String, EventoJogo> eventos;
    /*
        Scanner para leitura do input do utilizador.
     */
    private final Scanner scanner = new Scanner(System.in);
    /*
        Evento atual.
     */
    private EventoJogo evento;

    /*
        Construtor do AmbienteJogo.
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
        Método que retorna o evento atual.
     */
    public EventoJogo getEvento() {
        return evento;
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
        Observar o ambiente implica retornar o evento atual do ambiente.
        Para efeitos visuais, o evento e tambem mostrado.
     */
    public Evento observar() {
        evento.mostrar();
        return evento;
    }

    /*
        Método que executa um comando sobre o ambiente.
        Neste caso, os comandos nao tem efeito sobre o ambiente, e apenas sao mostrados.
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
