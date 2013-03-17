# -*- coding: utf-8 -*-

"""
Algoritmo de Dijkstra (com lista de adjascencias)
Autores: 
    Edsger Dijkstra
Colaborador:
 	Péricles Lopes Machado (pericles.raskolnikoff@gmail.com)
Tipo: 
    graphs
Descrição: 
    O Algoritmo de Dijsktra é um algoritmo em grafos clássico que determina a
    menor distância de um determinado vértice para todos os outros. Essa é a
    implementação utilizando matriz de adjacências, que tem desempenho 
    inferior.
Complexidade: 
    O(|E| log |V|)
Dificuldade: 
    medio
Referências:
    [1] http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    [2] Cormem, Thomas H. Introduction to Algorithms, 3rd Edition. 
        ISBN 978-0-262-53305-8. Páginas 658-659.
"""

from heapq import *;

"""
Função para imprimir rota
"""

def imprime_rota(pi, u):
	if pi[u] != None:
		imprime_rota(pi, pi[u]);
	print " ", u;

"""
Lista de adjacência; Para cada nó 'u' é fornecida uma lista de pares (v, d), onde 'v' é um 
nó que está conectado a 'u' e 'd' é a distancia entre 'u' e 'v'
"""

G = [
	[(1, 2), (3, 4), (5, 3), (8, 9)], 
	[(2, 7), (4, 6), (7, 8)],
	[(4, 9), (7, 9)],
	[(1, 13), (4, 4), (6, 3), (2, 3)], 
	[(1, 23), (7, 4), (5, 3), (8, 1), (4, 9)], 
	[(3, 11), (4, 7), (8, 9)], 
	[(5, 2), (3, 5), (4, 3), (5, 9)], 
	[(1, 2), (7, 4), (5, 9), (6, 8)], 
	[(7, 2), (2, 3), (1, 1), (3, 1)], 
]; 


"""
Origem s e destino t
"""
s = 1;
t = 6;

N = len(G);

"""
Estimativa de distancia inicial
None representa o infinito e código pai usado para recuperar a rota
"""
D = [];
pi = [];

for i in range(0, N):
	D += [None];
	pi += [None];

"""
Priority queue utilizada para o acesso rápido a melhor estimativa
"""
Q = [];

D[s] = 0;
heappush(Q, (0, s));

"""
Enquanto a fila de prioridade não estiver vazia tente verificar se o topo
da fila é melhor opção de rota para se chegar nos adjascentes. Como o topo
já é o mínimo, então garante-se que D[u] já está minimizado no momento.
"""
while Q:
	u = heappop(Q)[1];
	for adj in G[u]:
		v = adj[0];
		duv = adj[1];
		if D[v] > D[u] + duv or D[v] == None:
			D[v] = D[u] + duv;
			pi[v] = u;
			heappush(Q, (D[v], v));

if D[t] != None:
	print "Distância(", s, ",", t, ") = ", D[t]; 
	print "Rota:";
	imprime_rota(pi, t);
else:
	print "Não há rota entre os nós ", s, " e ", t;


