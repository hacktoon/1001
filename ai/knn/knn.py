# coding: utf-8
'''
K-Nearest Neighboor (k-NN)
Autor:
    Belur V. Dasarathy
Colaborador:
    Adriano Melo <adriano@adrianomelo.com>
Tipo:
    artificial-intelligence
Descrição:
    Algoritmo de aprendizagem baseado em instâncias.
    Uma matriz é dada ao algoritmo contendo vetores e as classes que eles pertencem,
    um vetor não classificado é a segunda entrada do algoritmo. 
    A saída é a classe que o vetor não classificado pertence.
Complexidade:  
    O(n * m * k) = O(n)
    n: número de instâncias
    m: tamanho dos vetores
    k: K-primeiros vizinhos
Dificuldade:
    medio
Referências:
    Belur V. Dasarathy, ed (1991). Nearest Neighbor (NN) Norms: NN Pattern Classification Techniques. ISBN 0-8186-8930-7.
'''

def knn(treino, padrao, distancia=lambda a,b: sum([(c-d)**2 for c,d in zip(a,b)])):
	return min([[distancia(pe[:-1], padrao), pe[-1]] for pe in treino])[1]

treino = [
		[1,2,3,4,5,6,'classe 1'],
        [1,2,3,3,5,6,'classe 1'],
        [2,3,5,6,7,8,'classe 2']]

print knn(treino, [2,3,4,6,7,8])

