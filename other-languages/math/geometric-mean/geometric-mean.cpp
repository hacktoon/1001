/*
Média geométrica
Autor: 
    ?
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo:
    math
Descrição: 
    É um algoritmo simples para calcular a média geométrica de n números
    reais utilizando o método de média de logaritmos (que é mais numericamente
    estável e computacionalmente mais eficiente que multiplicar
    todos os números e tirar a raiz, além de evitar o problema de overflow).
Complexidade de tempo: 
    O(n)
Dificuldade: 
    facil
Referências:
    http://en.wikipedia.org/wiki/Geometric_mean
    http://en.wikipedia.org/wiki/Numeric_stability
*/

#include <cstdio>
#include <cmath>

double geometric_mean(double values[], int n) {
    double sum = 0.0;
    
    for (int i = 0; i < n; i++)
        sum += log(values[i]);
    
    sum /= n;
    return exp(sum);
}

int main( ) {
    double values[] = {1, 2, 3, 4, 5};
    printf("%.10f\n", geometric_mean(values, 5));
    return 0;
}
