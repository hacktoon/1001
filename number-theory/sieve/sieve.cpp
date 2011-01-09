/*
Crivo de Eratóstenes
Autor:
    Eratóstenes de Cirene
Colaborador:
    ?
Tipo:
    number-theory
Descrição:
    O Crivo de Eratóstenes implementado em C++. É um algoritmo que
    serve para encontrar todos os números primos até um limite especificado.
Complexidade:
    O(n log log n)
Dificuldade:
    medio
Referências: 
    [1] http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    [2] http://mathworld.wolfram.com/SieveofEratosthenes.html
*/

#include <iostream>
#include <cmath>

/* 
A função pede dois parâmetros: 
    - primo: um array de booleanos
    - n: o tamanho do array primo
Após a execução do algoritmo, o vetor primo será tal que o valor da i-ésima
posição será true se (i + 1) for primo, ou false caso contrário. (O 1 somado
se deve ao fato de C++ ser uma linguagem com arrays que começam em 0.
*/

void eratostenes(bool primo[], int n) {
    int i, j, parada;
    
    primo[0] = false; 
    for (i = 1; i < n; i++) {
        primo[i] = true;
    }
    
    parada = (int) sqrtf(n);
    
    for (i = 1; i < parada; i++) {
        if ( primo[i] == false ) 
            continue;
        for (j = 2*i + 1; j < n; j += (i + 1)) 
            primo[j] = false;
    }
}

int main( ) {
    
    const int n = 25;
    bool primo[n];
    
    eratostenes(primo, n);
    
    for (int i = 0; i < 25; i++)
        std::cout << i + 1 << " " << primo[i] << "\n"; 

    return 0;
}
