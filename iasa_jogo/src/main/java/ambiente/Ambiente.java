package ambiente;

/*
    Interface que representa um ambiente.
    Um ambiente pode ser real ou virtual.

    O uso de interfaces neste caso é um exemplo de encapsulamento, os detalhes da implementação de um ambiente são
    ocultados pelo contrato definido pela interface.

    O uso de interfaces traz maior coesão e menor acoplamento.

    Nesta interface existe uma dependência para Evento e para Comando, visto que são usados como parametros
    pelos métodos definidos pela interface.

 */
public interface Ambiente {
    void evoluir();
    Evento observar();
    void executar(Comando comando);
}
