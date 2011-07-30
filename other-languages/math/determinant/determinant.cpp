/*
Determinante de matriz (utilizando decomposição LU)
Autor: 
    Carl Friedrich Gauss
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo: 
    math
Descrição: 
    É o algoritmo que calcula o determinante de uma matriz utilizando a
    decomposição LU como base. Como as matrizes L e U são triangulares, 
    o determinante delas são o produto das diagonais. Como o determinante de
    L é sempre 1, o determinante da matriz original A é igual ao determinante
    da matriz U.
Complexidade: 
    O(n³)
Dificuldade: 
    medio
Referências:
    http://en.wikipedia.org/wiki/Lu_decomposition
    http://en.wikipedia.org/wiki/Determinant
    http://mathworld.wolfram.com/LUDecomposition.html
    Cormem, Thomas H. Introduction to Algorithms, 3rd Edition.
        ISBN 978-0-262-53305-8. Página 821
*/

#include <iostream>
#include <stdio.h>

const int n = 4;

void lu_decomposition(float A[n][n], float U[n][n]) {
    float _A[n][n], L[n][n];
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

float determinant(float A[n][n]) {
    float U[n][n];
    float result = 1.0f;
    
    lu_decomposition(A, U);
    
    for (int i = 0; i < n; i++)
        result *= U[i][i];
        
    return result;
}

int main( ) {
    float A[n][n] = {
        {2.0,  3.0,  1.0,  5.0},
        {6.0, 13.0,  5.0, 19.0},
        {2.0, 19.0, 10.0, 23.0},
        {4.0, 10.0, 11.0, 31.0}};

    printf("Determinant: %.2f", determinant(A));

    return 0;
}
