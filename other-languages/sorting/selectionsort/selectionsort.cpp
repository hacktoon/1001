/*
Selection Sort
Autor: 
    ?
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo: 
    sorting
Descrição: 
    É um algoritmo de ordenação que consiste em pesquisar o menor elemento
    e colocar na primeira posição, o segundo menor e colocar na segunda 
    posição e assim sucessivamente, até que a sequência esteja ordenada.
    É uma excelente escolha quando há necessidade quando o custo de 
    escrita é alto, pois ele realiza em torno de 2n operações de escrita. [2]
Complexidade de tempo: 
    O(n²)
Dificuldade: 
    facil
Referências:
    [1] http://en.wikipedia.org/wiki/Selection_sort
    [2] http://en.wikipedia.org/wiki/Selection_sort#Comparison_to_other_sorting_algorithms
*/

#include <iostream>

void selection_sort(int a[], int n) {
    int i, j, min;
    int temp;
    
    for (i = 0; i < n-1; i++) {
        min = i;
        // encontra o menor elemento
        for (j = i + 1; j < n; j++)
            if ( a[j] < a[min] )
                min = j;
                
        // insere o menor elemento encontrado na posição correta
        temp = a[i];
        a[i] = a[min];
        a[min] = temp;
    }
}

int main( ) {
    int a[] = {6, -2, 3, 5, 7, 4, 3};
    
    selection_sort(a, 7);
    
    for (int i = 0; i < 7; i++)
        std::cout << a[i] << " ";
    
    return 0;
}
