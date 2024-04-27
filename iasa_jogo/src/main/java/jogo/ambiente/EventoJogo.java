package jogo.ambiente;

import ambiente.Evento;

/*
    Enumerado que representa os eventos possiveis do ambiente do jogo
 */
public enum EventoJogo implements Evento {
    SILENCIO, RUIDO, ANIMAL, FUGA, FOTOGRAFIA, TERMINAR;


    /*
        Metodo que mostra o comando, escrevendo-o na consola.
     */
    @Override
    public void mostrar() {
        System.out.printf("Evento: %s\n", this);
    }
}
