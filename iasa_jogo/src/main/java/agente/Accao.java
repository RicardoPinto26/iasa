package agente;

import ambiente.Comando;

/*
    Classe que representa uma acção do agente.
 */
public class Accao {
    /*
        Comando associado à acção do agente.
        Privado para garantir a restrição read-only.
     */
    private Comando comando;

    /*
        Método que devolve o comando associado à acção do agente.
     */
    public Comando getComando() {
        return comando;
    }

    /*
        Construtor da classe Accao.
     */
    public Accao(Comando comando) {
        this.comando = comando;
    }
}
