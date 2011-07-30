/*
Transposição de matrizes
Autor: 
    ?
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo:
    math
Descrição: 
    Calcula a matriz tranposta de uma matriz qualquer, ou seja, a matriz
    resultante da troca das linhas pelas colunas.
Complexidade de tempo: 
    O(m*n)
Dificuldade: 
    facil
Referências:
    http://en.wikipedia.org/wiki/Transpose
*/

#include <iostream>

const int m = 3;
const int n = 4;

double transpose(int a[m][n], int b[n][m]) {
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            b[j][i] = a[i][j];
}

int main( ) {
    int a[m][n] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}};
    int b[n][m];
    int i, j;
        
    transpose(a, b);
        
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) 
            std::cout << b[i][j] << " "; 
        std::cout << "\n";
    }

    return 0;
}
