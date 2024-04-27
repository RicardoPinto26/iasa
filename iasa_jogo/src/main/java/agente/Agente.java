package agente;

import ambiente.Ambiente;
import ambiente.Evento;

/*
    Classe que representa um agente.
    Um agente inteligente tem um ciclo percepção-processamente-acção.
    O agente percepciona o ambiente, processa essa precepção e actua sobre o ambiente.

    Nesta classe existe uma associação com Ambiente, visto que Ambiente é um atributo de Agente.
    Existe também uma composição com controlo.
 */
public class Agente {
    private Ambiente ambiente;
    private Controlo controlo;

    /*
        Contrutor do Agente.
     */
    public Agente(Ambiente ambiente, Controlo controlo) {
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    /*
        Método que executa o ciclo percepção-processamento-acção.
     */
    public void executar() {
        Percepcao percepcao = percepcionar();
        Accao accao = controlo.processar(percepcao);
        actuar(accao);
    }

    /*
        Método que percepciona o ambiente.
     */
    protected Percepcao percepcionar() {
        Evento evento = ambiente.observar();
        return new Percepcao(evento);
    }

    /*
        Método que actua sobre o ambiente.
     */
    protected void actuar(Accao accao) {
        if (accao != null) ambiente.executar(accao.getComando());
    }
}
