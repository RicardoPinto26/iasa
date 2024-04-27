package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

/*
    Classe responsável pela execução do jogo.
 */
public class Jogo {
    /*
        Atributos do jogo.
        Privados para diminuir o acoplamento.
     */
    private static AmbienteJogo ambiente;
    private static Personagem personagem;

    /*
        Método principal do jogo.
     */
    public static void main(String[] args) {
        ambiente = new AmbienteJogo();
        personagem = new Personagem(ambiente);

        executar();
    }

    /*
        Método responsável pelo game loop.
     */
    private static void executar() {
        do {
            ambiente.evoluir();
            personagem.executar();
        } while (ambiente.getEvento() != EventoJogo.TERMINAR);
    }
}
