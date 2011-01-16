/*
Fisher–Yates shuffle, Knuth shuffle (Durstenfeld's Solution)
Autor:
    Ronald Fisher, Frank Yattes, Donald Knuth, Richard Durstenfeld
Colaborador:
    Anderson "Cacovsky" Marques Ferraz
    amarquesferraz@gmail.com
Tipo:
    sorting
Descrição:
    Embaralha um vetor de numeros sequenciais. Nao utiliza nenhum vetor
    auxiliar (in-place) e so realiza tantos sorteios quanto posicoes do
    vetor.
Complexidade:
    O(n)
Dificuldade:
    medio
Referências:
    http://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
Licenca:
    LGPL
*/



#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
  * gera uma lista ordenada
  */
int * gera_vetor_ordenado(int qtde_elementos)
{
    int i;
    int *resultado= (int*) malloc(qtde_elementos*sizeof(int));

    for (i=0; i<qtde_elementos; i++)
        resultado[i] = i;

    return resultado;
}


void imprime_vetor(int *vetor, int qtde_elementos )
{
    int i;
    for (i=0; i<qtde_elementos; i++)
        printf("%d ", vetor[i]);

    printf("\n");
}


int main()
{
    //setup
    int N = 10;
    int *elementos = gera_vetor_ordenado(N); //passo 1
    srand ( time(NULL) ); //inicializando a seed

    printf("Vetor ordenado: ");
    imprime_vetor(elementos, N);

    //core
    int elementos_restantes = N;
    while (elementos_restantes>0){
        int k = rand() % (elementos_restantes); //passo 2

        //passo 3
        int tmp = elementos[k];
        elementos[k] = elementos[elementos_restantes-1];
        elementos[elementos_restantes-1] = tmp;

        elementos_restantes--; //passo 4
    }

    printf("Vetor embaralhado: ");
    imprime_vetor(elementos, N);

    return 0;
}
