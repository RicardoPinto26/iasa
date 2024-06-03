package agente;

import ambiente.Evento;

/*
    Classe que representa a percepcao do agente.
    Uma percepcao e uma pedaco de informacao que o agente consegue obter do ambiente.

    Temos uma associacao com a classe Evento. A instancia de Evento e descrita como read only. Para garantir esta
    restricao, encapsulamos o atributo evento (isto e, tornamos o atributo privado) e disponibilizamos um
    metodo getEvento() que devolve o Evento associado. Deste modo, a instancia de Evento nao pode ser alterada por
    outras classes.
 */
public class Percepcao {
    /*
        Evento associado à percepção do agente.
        Privado para garantir a restrição read-only.
     */
    private Evento evento;

    /*
        Construtor da classe Percepcao.
     */
    Percepcao(Evento evento) {
        this.evento = evento;
    }

    /*
        Método que devolve o evento associado à percepção do agente.
     */
    public Evento getEvento() {
        return evento;
    }
}
