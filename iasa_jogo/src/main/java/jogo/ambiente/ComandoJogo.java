package jogo.ambiente;

import ambiente.Comando;

/*
    Enumerado que representa os comandos possiveis do jogo sobre o ambiente.
 */
public enum ComandoJogo implements Comando {
    PROCURAR, APROXIMAR, OBSERVAR, FOTOGRAFAR;

    /*
        Metodo que mostra o comando, escrevendo-o na consola.
     */
    @Override
    public void mostrar() {
        System.out.printf("Comando: %s\n", this);
    }
}
