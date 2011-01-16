/*
Valida solução de sudoku
Autor:
    ?
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo:
    puzzle
Descrição:
    Algoritmo que verifica se um jogo de sudoku está corretamente preenchido
    ou não, de acordo com as regras do jogo.
    Utiliza a ideia de que, se um conjunto tem somente de 1 a 9 sem duplicidade, 
    então a soma de todos os elementos é constante.
Complexidade:
    O(1)
Dificuldade:
    facil
Referências:
    http://en.wikipedia.org/wiki/Sudoku
*/

#include <iostream>

bool validate_sudoku(int sudoku[9][9]) {
    // 1 + 2 + 3 + 4 + ... + 9
    const int SUM_9 = 45;

    // inicializa somas com 0 
    int sum_line[9], sum_column[9], sum_matrix[3][3];
    
    int i, j;

    for (i = 0; i < 9; i++)
        sum_line[i] = sum_column[i] = sum_matrix[i/3][i%3] = 0;
    
    
    for (i = 0; i < 9; i++)
        for (j = 0; j < 9; j++) {           
            sum_line[i] += sudoku[i][j];
            sum_column[j] += sudoku[i][j];
            sum_matrix[i/3][j/3] += sudoku[i][j];
        } 
            
    for (i = 0; i < 9; i++)
        if ( sum_column[i] != SUM_9 || sum_line[i] != SUM_9 || sum_matrix[i/3][i%3] != SUM_9 )
            return false;
        
    return true;    
}

int main( ) {

    int game[9][9] = {
        {5, 3, 4, 6, 7, 8, 9, 1, 2},
        {6, 7, 2, 1, 9, 5, 3, 4, 8},
        {1, 9, 8, 3, 4, 2, 5, 6, 7},
        {8, 5, 9, 7, 6, 1, 4, 2, 3},
        {4, 2, 6, 8, 5, 3, 7, 9, 1},
        {7, 1, 3, 9, 2, 4, 8, 5, 6},
        {9, 6, 1, 5, 3, 7, 2, 8, 4},
        {2, 8, 7, 4, 1, 9, 6, 3, 5},
        {3, 4, 5, 2, 8, 6, 1, 7, 9}};

    std::cout << validate_sudoku(game);
    
    return 0;
}
