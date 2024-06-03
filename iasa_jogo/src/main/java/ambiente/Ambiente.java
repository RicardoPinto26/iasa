package ambiente;

/*
    Interface que representa um ambiente.
    A representacaao do ambiente e um elemento de suporte do processamento interno em
    alguns modelos de agente inteligente. Essas representacoes podem ter diferentes niveis
    de complexidade.

    Um ambiente tem diversas propriedades:
    - Discreto ou continuo -  Se for discreto (como no caso de um ambiente virtual), este
        acontece num tempo nao continuo, ou seja, os seus pontos de informacao tem
        um intervalo temporal. Se for continuo (como no caso de um ambiente real), este
        acontece num tempo continuo, ou seja, existem infinitos pontos de informacao.

    - Deterministico/Estocastico - Se for deterministico, o ambiente opera sempre da
        mesma forma, ou seja, cada accao leva a um resultado expectavel. Se for estocastico,
        o ambiente opera de forma aleatoria, ou seja, mesmo sabendo toda a informacao
        do ambiente, nao e possivel determinar qual sera o resultado de uma accao sobre
        este.

    - Estatico/Dinamico - Um ambiente estatico nao varia, enquanto que um ambiente
        dinamico varia.

    - Totalmente/Parcialmente observavel - Se um ambiente for totalmente observavel,
        um agente podera ter toda a informacao contida no ambiente. Se o ambiente for
        apenas parcialmente observavel, apenas parte da informacao do ambiente esta
        disponivel para o agente.

    - Agente unico/Multiplos agentes - Um ambiente podera ter apenas um agente a
        atuar sobre este, um varios.

    Nesta interface existe uma dependencia para Evento e para Comando, visto que sao usados como parametros
    pelos métodos definidos pela interface, mas nao estao estruturalmente ligados a esta.

 */
public interface Ambiente {
    /*
        Metodo que evolui o ambiente.
     */
    void evoluir();

    /*
        Metodo para observar o ambiente.
     */
    Evento observar();

    /*
        Metodo para executar um comando no ambiente.
     */
    void executar(Comando comando);
}
