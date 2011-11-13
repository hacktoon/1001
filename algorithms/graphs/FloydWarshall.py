 
# -*- coding: utf-8 -*-

"""
Algoritmo de Floyd-Warshall.

Autor:
	Robert W. Floyd & Stephen Warshall (1962)

Colaborador:
	Pedro Arthur Duarte (JEdi)
	pedroarthur.jedi@gmail.com

Tipo:
	graph
	all-pairs shortest path in weighted graphs
	dynamic programming

Descrição:
	O algoritmo de Floyd-Warshall computa os caminhos mais curtos entre todos os pares de um grafo valorado de pesos arbitrários.

	A formulação em programação dinâmica para esse problema consiste em
	determinar de forma bottom-up os menores caminhos para todos os vértices
	considerando que os caminhos intermediários consistem apenas de um
	subconjunto de vértices. Assim, $d_{ij}^{(k)}$ é menor caminho do vértice
	$i$ ao vértice $j$ tal que esse caminho consiste apenas de vértices
	intermediários em $k$. Assim, a seguinte formulação é empregada no
	algoritmo de Floyd-Warshall:

	$$ d_{ij}^{(k)} = min(d_{ij}^{(k)}, d_{ik}^{(k-1)} + d_{kj}^{(k-1)}) $$

	Essa formulação assuma que $d_{ij} = 0$ se $i=j$, e $d_{ij}=\infty$ se não
	há uma aresta entre os vértices $i$ e $j$.

Complexidade:
	Θ(V³),  onde 'V' é a cardinalidade o conjunto de vértices.

Dificuldade:
	média

Referências:
	Cormen; Leiserson; Rivest; Stein. Introduction to Algorithms (2 ed). ISBN: 978-0262033848.
	https://secure.wikimedia.org/wikipedia/en/wiki/Floyd–Warshall_algorithm

Licença:
  GPLv3

"""

from sys import maxint as Infinity

class NoSuchAPathError(Exception):
	pass

class FloydWarshall:
	def __init__(self, matrix):
		self.matrix = [ ]
		self.paths = [ ]

		for r in matrix:
			self.matrix.append([ ])
			self.paths.append([ ])

			for c in r:
				self.matrix[-1].append(c)
				self.paths[-1].append(None)

	def shortestPaths(self):
		for k in xrange(0, len(self.matrix)):
			for i in xrange(0, len(self.matrix)):
				for j in xrange(0, len(self.matrix)):
					if self.matrix[i][k] + self.matrix[k][j] < self.matrix[i][j]:
						self.matrix[i][j] = self.matrix[i][k] + self.matrix[k][j]
						self.paths[i][j] = k

		return self

	def getItermediate(self, source, destination):
		if self.matrix[source][destination] == Infinity:
			raise NoSuchAPathError

		intermediate = self.paths[source][destination]

		if intermediate is None:
			return [ ]

		return (self.getItermediate(source, intermediate)
					+ [ intermediate ]
						+ self.getItermediate(intermediate, destination))

	def getPath(self, source, destination):
		return ([ source ]
					+ self.getItermediate(source, destination)
						+ [ destination ])

graph = [
	[0, 6, 8, 3, 5, 3, 2, 7, 1, 2, ],
	[0, 0, 2, 9, 1, 6, 2, 9, 9, 7, ],
	[6, 8, 0, 5, 8, 5, 7, 9, 8, 2, ],
	[6, 9, 7, 0, 8, 9, 8, 6, 3, 4, ],
	[0, 4, 8, 1, 0, 5, 8, 0, 7, 9, ],
	[2, 3, 3, 9, 9, 0, 0, 3, 0, 4, ],
	[7, 8, 0, 7, 7, 2, 0, 6, 0, 8, ],
	[3, 3, 5, 4, 8, 8, 8, 0, 4, 0, ],
	[9, 7, 2, 5, 0, 5, 4, 9, 0, 3, ],
	[6, 1, 8, 6, 6, 6, 1, 6, 7, 0, ],
]

print FloydWarshall(graph).shortestPaths().getPath(1,9)
