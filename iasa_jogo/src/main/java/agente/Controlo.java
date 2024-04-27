package agente;

/*
    Interface que representa o controlo de um agente.
    O Controlo do agente é responsável pelo processamento de uma percepção, e da consequente
    decisão sobre que acção tomar.
 */
public interface Controlo {
    /*
        Método que processa uma percepcao, retornando a accao correspondente.
     */
    Accao processar(Percepcao percepcao);
}
