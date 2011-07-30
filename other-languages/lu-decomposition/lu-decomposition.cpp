/*
Decomposição LU
Autor: 
    Carl Friedrich Gauss
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo: 
    math
Descrição: 
    É o algoritmo que decompõe uma matriz quadrada A qualquer em um produto de duas
    matrizes L e U, onde L é uma matriz triangular inferior e U uma matriz triangular
    superior. É útil porque é computacionalmente mais simples trabalhar com matrizes
    triangulares que com matrizes completas.
Complexidade: 
    O(n³)
Dificuldade: 
    medio
Referências:
    http://en.wikipedia.org/wiki/Lu_decomposition
    http://mathworld.wolfram.com/LUDecomposition.html
    Cormem, Thomas H. Introduction to Algorithms, 3rd Edition.
        ISBN 978-0-262-53305-8. Página 821
*/

#include <iostream>
#include <stdio.h>

const int n = 4;

void lu_decomposition(float A[n][n], float L[n][n], float U[n][n]) {
    float _A[n][n];
    int i, j, k;

    // copia para evitar modificações na matriz original
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            _A[i][j] = A[i][j];

    // inicializa a matriz U com zeros
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            U[i][j] = 0;
            
    // inicializa a matriz L com 0s acima da diagonal e 1s na diagonal
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            if ( i < j )
                L[i][j] = 0;
            else if ( i == j )
                L[i][j] = 1;
                
    for (k = 0; k < n; k++) {
        U[k][k] = _A[k][k];
        
        for (i = k + 1; i < n; i++) {
            L[i][k] =  _A[i][k]/U[k][k];
            U[k][i] = _A[k][i];
        }
    
        
        for (i = k + 1; i < n; i++)
            for (j = k + 1; j < n; j++)
                _A[i][j] -= L[i][k]*U[k][j];            
    }
}

int main( ) {
    float A[n][n] = {
        {2.0,  3.0,  1.0,  5.0},
        {6.0, 13.0,  5.0, 19.0},
        {2.0, 19.0, 10.0, 23.0},
        {4.0, 10.0, 11.0, 31.0}};
    float L[n][n], U[n][n];
    int i, j;
    
    lu_decomposition(A, L, U);
    
    for (i = 0; i < n; i++) {       
        printf("[ ");
        
        for (j = 0; j < n; j++)
            printf("%.2f ", L[i][j]);
        
        printf("] [ ");
        
        for (j = 0; j < n; j++)
            printf("%.2f ", U[i][j]);
        
        printf("]\n");
    }

    return 0;
}
