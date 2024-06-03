package agente;

import ambiente.Comando;

/*
    Classe que representa uma accao do agente.
    Uma accao e uma interaccao do agente com o ambiente.

    Temos uma associacao com a classe Comando. A instancia de Comando e descrita como read only. Para garantir esta
    restricao, encapsulamos o atributo comando (isto e, tornamos o atributo privado) e disponibilizamos um
    metodo getComando() que devolve o comando associado. Deste modo, a instancia de Comando nao pode ser alterada por
    outras classes.
 */
public class Accao {
    /*
        Comando associado a accao do agente.
     */
    private Comando comando;

    /*
        Construtor da classe Accao.
     */
    public Accao(Comando comando) {
        this.comando = comando;
    }

    /*
        Metodo que devolve o comando associado a accao do agente.
     */
    public Comando getComando() {
        return comando;
    }
}
