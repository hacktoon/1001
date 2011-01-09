/*
Menor e maior elemento simultâneo
Autor: 
    ?
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo: 
    search
Descrição: 
    É um algoritmo que pesquisa o menor e o maior elemento do vetor
    simultaneamente, economizando, assim, comparações. Enquanto utizando 
    pesquisa de menor e maior elementon separadamente são necessárias
    2n-2 comparações, com esse algoritmo, o número de comparações é reduzido
    para aproximadamente 1,5n. [1]
    O algoritmo funciona da seguinte forma: divide-se o vetor em pares, compara-se
    os dois elementos dos pares, compara-se o menor com o valor minimo armazenado
    e o maior com o valor máximo armazenado, assim, tem um custo de 3 comparações
    para cada 2 elementos, resultando em aproximadamente 1,5n comparações.
Complexidade:
    O(n)
Dificuldade: 
    facil
Referências:
    [1] Cormem, Thomas H. Introduction to Algorithms, 3rd Edition, páginas 214-215
*/

#include <iostream>

/*
Parâmetros:
a: o vetor
n: o número de elementos
min: variável para armazenar a posição do menor valor
max: variável para armazenar a posição do maior valor
*/

void min_max(int a[], int n, int &min, int &max) {
    int i = 0;
    
    min = max = 0;
    // valida o caso do número de elementos ser ímpar
    if ( n % 2 != 0 ) {
        i = 1;
    }
    
    for (; i < n; i += 2) {
        if ( a[i] < a[i + 1] ) {
            if ( a[i] < a[min] )
                min = i;
            if ( a[i + 1] > a[max] )
                max = i + 1;
        } else {
            if ( a[i + 1] < a[min] )
                min = i + 1;
            if ( a[i] > a[max] )
                max = i;
        }
    }
}

int main( ) {
    
    int a[] = {8, 2, 5, 3, 1, 7, 6, 4};
    int min, max;
    
    min_max(a, 8, min, max);
    std::cout << "Menor valor: " << a[min] << "\n";
    std::cout << "Maior valor: " << a[max] << "\n"; 
    
    return 0;
}
