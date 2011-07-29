 
/*
Stooge Sort
Autores: 
    Morris Howard, Lawrence Fine, Jerome Howard 
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo: 
    sorting
Descrição: 
    É um algoritmo de ordenação recursivo bem de fácil implementação: verifica 
    se o primeiro elemento é maior que o último, ordena os 2 primeiros terços 
    do vetor, ordena os 2 ultimos e ordena os dois primeiros novamente. Apesar 
    de elegante, é um algoritmo bem lento (pior até que o bubble sort).
Complexidade: 
    O(n^2.701)
Dificuldade: 
    facil
Referências:
    [1] http://en.wikipedia.org/wiki/Stooge_sort
*/

#include <iostream>

void stooge_sort(int a[], int left, int right) {
    if ( a[left] > a[right] ) {
        int temp = a[left];
        a[left] = a[right];
        a[right] = temp;
    }
    
    if ( right-left > 1 ) {
        int k = (right-left+1)/3;
        stooge_sort(a, left, right-k);
        stooge_sort(a, left+k, right);
        stooge_sort(a, left, right-k);
    }
}

int main( ) {
    int a[] = {6, -2, 3, 5, 7, 4, 10, 3};
    
    stooge_sort(a, 0, 7);
    
    for (int i = 0; i < 8; i++)
        std::cout << a[i] << " ";
    
    return 0;
}
