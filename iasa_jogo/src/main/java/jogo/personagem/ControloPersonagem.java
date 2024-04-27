package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maqest.Estado;
import maqest.MaquinaEstados;

/*
    Classe que representa o controlo da personagem.
    Usa uma máquina de estados para controlar o comportamento da personagem.
 */
public class ControloPersonagem implements Controlo {
    private MaquinaEstados maqEst;

    public Estado getEstado() {
        return maqEst.getEstado();
    }

    /*
        Construtor da classe.

        Inicia os estados possiveis da máquina de estados, adicionando todas as transicoes possiveis.
        De seguida, inicia a maquina de estados com o estado inicial, neste caso: Procura.
     */
    public ControloPersonagem() {
        Estado procura = new Estado("Procura");
        Estado inspeccao = new Estado("Inspeccao");
        Estado observacao = new Estado("Observacao");
        Estado registo = new Estado("Registo");

        Accao procurar = new Accao(ComandoJogo.PROCURAR);
        Accao aproximar = new Accao(ComandoJogo.APROXIMAR);
        Accao observar = new Accao(ComandoJogo.OBSERVAR);
        Accao fotografar = new Accao(ComandoJogo.FOTOGRAFAR);


        procura
                .transicao(EventoJogo.SILENCIO, procura, procurar)
                .transicao(EventoJogo.RUIDO, inspeccao, aproximar)
                .transicao(EventoJogo.ANIMAL, observacao, aproximar);

        inspeccao
                .transicao(EventoJogo.RUIDO, inspeccao, procurar)
                .transicao(EventoJogo.SILENCIO, procura)
                .transicao(EventoJogo.ANIMAL, observacao, aproximar);

        observacao
                .transicao(EventoJogo.FUGA, inspeccao)
                .transicao(EventoJogo.ANIMAL, registo, observar);

        registo
                .transicao(EventoJogo.FUGA, procura)
                .transicao(EventoJogo.FOTOGRAFIA, procura)
                .transicao(EventoJogo.ANIMAL, registo, fotografar);


        maqEst = new MaquinaEstados(procura);
    }

    /*
        Utiliza a máquina de estados para processar a percepçao (neste caso, o seu evento) e para
         escolher a accao correspondente à percepção.
     */
    @Override
    public Accao processar(Percepcao percepcao) {
        Evento evento = percepcao.getEvento();
        Accao accao = maqEst.processar(evento);
        mostrar();
        return accao;
    }

    /*
        Método que mostra o estado atual da máquina de estados.
     */
    private void mostrar() {
        System.out.printf("Estado: %s\n", getEstado().getNome());
    }
}
