package jogo.personagem;

import agente.Agente;
import jogo.ambiente.AmbienteJogo;

/*
    Classe que representa a personagem do jogo.
    Esta extende Agente, visto que a personagem do jogo e um agente inteligente.

    A heranca de Agente é um exemplo de factorização estrutural.
 */
public class Personagem extends Agente {
    /*
        Construtor da classe.
     */
    public Personagem(AmbienteJogo ambiente) {
        super(ambiente, new ControloPersonagem());
    }
}
