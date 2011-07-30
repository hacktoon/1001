/*
Multiplicação de matrizes (método trivial)
Autor: 
    ?
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo: 
    math
Descrição: 
    É o algoritmo trivial para multiplicação de duas matrizes A e B, onde 
    A é uma matriz m x n e B é uma matriz n x p, a partir da definição 
    matemática.
Complexidade de tempo: 
    O(m*n*p)
Dificuldade: 
    facil
*/

#include <iostream>

const int m = 3;
const int n = 5;
const int p = 4;

/*
Parâmetros:
a: matriz (m x n)
b: matriz (n x p)
c: matriz para armazenar o resultado (m x p) 
*/

void matrix_multiplication(int a[m][n], int b[n][p], int c[m][p]) {
    int i, j, k;
    
    for (i = 0; i < m; i++)
        for (j = 0; j < p; j++)
            c[i][j] = 0;
    
    for (i = 0; i < m; i++)
        for (j = 0; j < p; j++)
            for (k = 0; k < n; k++) 
                c[i][j] += a[i][k] * b[k][j];
}

int main( ) {

    int a[m][n] = { 
        {1, 2, 3, 4, 5},
        {6, 7, 8, 9, 10},
        {11, 12, 13, 14, 15}};
    int b[n][p] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16},
        {17, 18, 19, 20}};  
    int c[m][p];
    
    matrix_multiplication(a, b, c);
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) 
            std::cout << c[i][j] << " ";
        std::cout << "\n";
    }

    return 0;
}
