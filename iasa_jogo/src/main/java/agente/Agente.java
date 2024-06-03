package agente;

import ambiente.Ambiente;
import ambiente.Evento;

/*
    Classe que representa um agente inteligente. Um agente inteligente e a representacao computacional de um
    sistema autonomo inteligente. Um agente inteligente opera num ciclo realimentado percepcao-processamento-accao.
    Atraves deste ciclo, e realizado o controlo da funcionalidade do sistema, de modo a cumprir a sua finalidade.
    Ou seja, o agente percepciona o ambiente, processa essa precepcao e actua sobre o ambiente.

    Nesta classe existe uma associação com Ambiente, visto que Ambiente é um atributo de Agente.
    Existe também uma composição com Controlo, visto que o Controlo so existe no contexto do Agente.
 */
public class Agente {
    private Ambiente ambiente;
    private Controlo controlo;

    /*
        Construtor do Agente.
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
        Percepcionar e o processo de obter informacao do ambiente, ou seja, observa-lo.
        Neste caso, a observacao do ambiente retorna um evento, que e encapsulado numa percepcao.
     */
    protected Percepcao percepcionar() {
        Evento evento = ambiente.observar();
        return new Percepcao(evento);
    }

    /*
        Método que actua sobre o ambiente.
        Actuar e o processo de interagir com o ambiente.
        Neste caso, a interacao com o ambiente e feita atraves de um comando, que esta encapsulado numa accao.
     */
    protected void actuar(Accao accao) {
        if (accao != null) ambiente.executar(accao.getComando());
    }
}
