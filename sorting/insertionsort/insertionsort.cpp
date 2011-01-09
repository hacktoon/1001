/*
InsertionSort
Autor:
    ?
Colaborador:    
    Willian
Tipo:
    sorting
Descrição:
    Varre o vetor organizando-o em ordem crescente.
    Só pula para o próximo elemento depois de organizar todos os elementos anteriores.
Complexidade:
    O(n²)
Dificuldade:
    facil
Referências:
    http://pt.wikipedia.org/wiki/Insertion_sort
*/

#include <iostream>

using namespace std;

/*
 * Parâmetros
 * int vetor[]
 *      Vetor de números inteiros
 * int tam
 *      Quantidade de elementos do vetor 'vetor[]'
 */
void insertionSort(int vetor[], int tam)
{
    //Vamos começar o loop pelo segundo elemento do vetor
    for(int i=1;i<tam;i++)
    {
        //A variável 'neddle' vai começar apontando um elemento antes de 'i'
        int anterior = i-1;

        // 'proximo' sempre aponta à frente de 'anterior'
        int proximo = anterior + 1;

        int tmp;

        //'troca' vai controlar a varredura no vetor
        bool troca = true;

        do
        {
            if(vetor[anterior] > vetor[proximo])
            {
                tmp = vetor[anterior];
                vetor[anterior] = vetor[proximo];
                vetor[proximo] = tmp;
            }
            else
                troca = false;

            anterior--;
            proximo = anterior + 1;

            //Verificando o limite do vetor
            if (anterior<0)
                troca = false;
        } while(troca);
    }
}

//exemplo de uso
int main(void)
{
    //Criando um vetor de testes
    int vetor[] = { 98, 78, 2, 4, 100, -2 };
    int tam = sizeof(vetor) / sizeof(int);

    //Chamando a função de ordenação com o vetor e o tamanho
    insertionSort(vetor, tam);

    //Imprimindo
    for(int i=0; i<tam; i++)
    {
        cout << vetor[i] << ' ';
    }

    return 0;
}
