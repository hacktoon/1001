/*
 * BuscaBinaria
 * Autor:
 *     Jon Bentley
 * Colaborador:
 *     Fabiano Sobreira
 * Tipo:
 *     search
 * Descrição:
 *     A pesquisa ou busca binária (em inglês binary search algorithm ou binary
 *     chop) é um algoritmo de busca em vetores que requer acesso aleatório aos
 *     elementos do mesmo. Ela parte do pressuposto de que o vetor está ordenado
 *     e realiza sucessivas divisões do espaço de busca (divisão e conquista)
 *     comparando o elemento buscado (chave) com o elemento no meio do vetor.
 * Complexidade:
 *     ?
 * Dificuldade:
 *     fácil
 * Referências:
 *     http://pt.wikipedia.org/wiki/Pesquisa_binária
 */
public class BuscaBinaria {

    private int[] vetor;
    private int valorProcurado;

    private int menor;
    private int maior;

    public BuscaBinaria(int[] vetor, int valorProcurado) {
        this.vetor = vetor;
        this.valorProcurado = valorProcurado;
        menor = 0;
        maior = vetor.length - 1;
    }

    public int getPosicao() {
        while (menor < maior) {
            int meio = menor + ((maior - menor) / 2);
            int valorMeio = vetor[meio];
            if (valorProcurado < valorMeio)
                maior = meio;
            else if (valorProcurado > valorMeio)
                menor = meio + 1;
            else
                return meio;
        }
        return -1;
    }

    /*
     * Método de exemplo para verificação do algorítimo. O algoritimo pode ser
     * executado da seguinte maneira: java BuscaBinaria 1000 799
     */
    public static void main(String[] args) {
        if (args.length < 2)
            throw new IllegalArgumentException("informe o tamanho do vetor e o valor procurado");
            
        int tamanho = Integer.parseInt(args[0]);
        int alvo = Integer.parseInt(args[1]);

        int[] vetor = new int[tamanho];
        for (int i = 0; i < vetor.length; i++)
            vetor[i] = i;

        BuscaBinaria bs = new BuscaBinaria(vetor, alvo);
        int resultado = bs.getPosicao();

        if (resultado == -1)
            System.out.println("Não encontrado.");
        else
            System.out.println("Encontrado na posição: " + resultado + ".");
    }
}
