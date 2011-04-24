# coding: utf-8
'''
Transposição de matrizes
Autor: 
    ?
Colaborador:
    Dayvid Victor (victor.dvro@gmail.com)
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
'''

def get_transpose(matrix):
	return [[c for c in [l[i] for l in matrix]] for i in range(len(matrix[0]))]

if __name__ == '__main__':
	matrix = [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5,6]]
	print matrix
	print get_transpose(matrix)
	
