/*
Shell Sort
Autor: 
    Donald Shell
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo: 
    sorting
Descrição: 
    É um método que funciona repetidamente ordenando com insertion sort
    elementos com uma distância, inicialmente grande e que vai diminuindo de 
    acordo com uma sequência, até que a distância é 1 e o vetor é finalmente
    ordenado.
Complexidade de tempo: 
    O(n^1.5)
Dificuldade: 
    medio
Referências:
    http://en.wikipedia.org/wiki/Shell_sort
    http://www.iti.fh-flensburg.de/lang/algorithmen/sortieren/shell/shellen.htm
*/

#include <iostream>

void shell_sort(int a[], int n) {
    int dist = 1;   
    int i, j, temp;
    
    // Essa implementação do Shell Sort utiliza incrementos da forma 2^k - 1:
    // 1, 3, 7, 15, 31, 63, 127, ...
    
    // Aqui é determinado qual é o incremento inicial:
    // o maior incremento da forma 2^k - 1 que não é menor que n
    while ( 2*dist < n ) 
        dist = 2*dist + 1;

    while ( dist > 0 ) {
    
        // Faz insertion sort com distancia dist (h-sort)
        for (i = dist; i < n; i++) {
            temp = a[i];
            
            for (j = i - dist; j >= 0 && temp < a[j]; j -= dist)
                a[j + dist] = a[j];
            
            a[j + dist] = temp;
        }
        
        // diminui a distância
        dist = dist / 2;
    }
}

int main( ) {
    int a[] = {6, -2, 3, 5, 7, 4, 3, 10, -1, 8};
    
    shell_sort(a, 10);
    
    for (int i = 0; i < 10; i++)
        std::cout << a[i] << " ";
        
    return 0;
}
