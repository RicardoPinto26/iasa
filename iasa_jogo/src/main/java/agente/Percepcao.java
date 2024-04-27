package agente;

import ambiente.Evento;

/*
    Classe que representa a percepção do agente.
 */
public class Percepcao {
    /*
        Evento associado à percepção do agente.
        Privado para garantir a restrição read-only.
     */
    private Evento evento;

    /*
        Método que devolve o evento associado à percepção do agente.
     */
    public Evento getEvento() {
        return evento;
    }

    /*
        Construtor da classe Percepcao.
     */
    Percepcao(Evento evento) {
        this.evento = evento;
    }
}
