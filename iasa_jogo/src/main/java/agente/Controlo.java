package agente;

/*
    Interface que representa o controlo de um agente.
    O Controlo do agente e responsavel pelo processamento de uma percepcao, e da consequente
    decisao sobre que accao tomar.

    Uma interface e um contrato que define um conjunto de atributos e de metodos que uma classe deve implementar,
    sem definir a implementacao dos mesmos.

    Tem duas dependencias: Percepcao e Accao, visto que a classe Controlo depende destas duas classes no metodo processar,
    mas nao esta estruturalmente associado a estas.
 */
public interface Controlo {
    /*
        Metodo que processa uma percepcao, retornando a accao correspondente.
     */
    Accao processar(Percepcao percepcao);
}
