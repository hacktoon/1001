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


import math, re
class knn(object):
    matrix = [[]] # matriz do tipo [  [a1, a2, a3, a4, a5, a6, classe], [...]  ]
    distancias = [] # array que terá o resultado do calculo das distancias entre o elemento de entrada e o conjunto de treinamento
    classes = {} # dicionário que conterá a contagem de cada classe, {'classe-A': 2, 'classeB': 1}

    def __init__(self, matriz):
        self.matrix = matriz

    def distancia(self, tupla):
    ''' calcula a distância de cada elemento de treinamento ao vetor de entrada '''
        self.distancias = []

        for linha in self.matrix:
            distancia = self._calc_distancia(tupla, linha)
            self.distancias.append((distancia, linha[-1]))

        self.distancias.sort()

    def _calc_distancia(self, tupla, linha):
	''' dados dois vetores, calcular a distancia euclidiana '''
        distancia = 0.0
        for i in xrange(len(tupla)):
            distancia += (float(tupla[i]) - float(linha[i])) ** 2 # distancia + (a1 - b1)²
        return math.sqrt(distancia)

    def classificar(self, tupla, K=3):
	''' Pega o array de distãncias calculado por distancia(tupla) e o ordena para classificar o ponto de entrada de acordo com o K passado como parâmetro'''
        self.classes = {}
        self.distancia(tupla)

        for dist in self.distancias[:K]:
            if self.classes.has_key(dist[1]):
                self.classes[dist[1]] += 1
            else:
                self.classes[dist[1]] = 1
        
        c = [(self.classes[a], a) for a in self.classes]
        c.sort()
        c.reverse()
        if len(c) >= 1 and len(c[0]) == 2:
            return c[0][1]

if __name__ == "__main__":
    treino = [
        [4, 3, 'classe 1'],
        [2, 3, 'classe 1'],
        [20, 20, 'classe 2'],
        [15, 20, 'classe 2']]

    KNN = knn(treino)

    print KNN.classificar([4, 5])
    print KNN.classificar([400, 500])
    print KNN.classificar([2, 3])

