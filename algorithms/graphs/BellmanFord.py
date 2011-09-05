# -*- coding: utf-8 -*-

"""
Algoritmo de Bellman-Ford.

Autor:
	Richard Bellman & Lester R. Ford Jr. (1958)

Colaborador:
	Pedro Arthur Duarte (JEdi)
	pedroarthur.jedi@gmail.com

Tipo:
	graph
	shortest path on directed graphs with negative weighted edges

Descrição:
	O algoritmo de Bellman-Ford determina o caminho mais curto de origem única
	em grafos com arestas de pesos negativos. Para grafos sem arestas negativas,
	o algoritmo de Dijkstra apresenta melhor desempenho.

Complexidade:
	O(V*E), onde 'V' é a cardinalidade o conjunto de vértices e 'E' a
	cardinalidade do conjunto de arestas.

Dificuldade:
	media

Referências:
	http://en.wikipedia.org/wiki/Bellman-Ford_algorithm

Licença:
	GPLv3

"""

from sys import maxint

class NegativeWeightCycleError(Exception):
	pass


class Vertex:
	'''
	Abstração de vértice para a implementação através de lista de adjacência;
	estão inclusos atributos extras para a implementação do algoritmo
	'''
	def __init__(self, label, distance, predecessors=None):
		self.label = label

		self.distance = distance
		self.predescessor = None

	def __repr__(self):
		return str(self.label)

class Edge:
	'''
	Abstração de aresta para a implementação através de lista de adjacência
	'''
	def __init__(self, source, destination, weight):
		self.src = source
		self.dst = destination
		self.wht = weight

class Graph:
	'''
	Abstração de grafo para a implementação através de lista de adjacência.
	'''
	def __init__(self, graph=None):
		'''
		Caso seja passada uma matriz de adjacência, essa é transformada numa
		lista de adjacência.
		'''
		self.vertex = { }
		self.edges = [ ]

		if graph == None:
			return

		for i in xrange(0, len(graph)):
			for j in xrange(0, len(graph)):
				if graph[i][j] == None:
					continue

				self.addEdge(i, j, graph[i][j])

	def addEdge(self, source, destination, weight):
		if source not in self.vertex:
			self.vertex[source] = Vertex(source, maxint)

		if destination not in self.vertex:
			self.vertex[destination] = Vertex(destination, maxint)

		self.edges.append(
			Edge(self.vertex[source], self.vertex[destination], weight))

class BellmanFord:
	def __init__(self, g):
		self.graph = g

	def adjacencyMatrixShortestPath(self, source, destination):
		'''Implementação através de matriz de adjacência'''

		# Etapa de inicialização: todas as distâncias são definidas como
		# infinitas para que sejam então atualizadas durante a relaxação
		self.distances = [ maxint for s in self.graph ]
		self.distances[source] = 0

		# Arranjo auxiliar para que possamos reconstruir o menor caminho
		self.predecessors = [ 0 for s in self.graph ]

		# Para cada v em V:
		for i in xrange(0, len(self.graph)):
			# Para cada e em E
			#	Aqui, devido ao uso da matriz de adjacência, precisamos
			#	utilizar dois laços "para" (for) de forma que possamos
			#	percorrer todas as aresta
			for u in xrange(0, len(self.graph)):
				for v in xrange(0, len(self.graph)):
					if self.graph[u][v] == None:
						continue

					# Etapa de "relaxação" do grafo
					if self.distances[u] + self.graph[u][v] < self.distances[v]:
						self.distances[v] = self.distances[u] + self.graph[u][v]
						self.predecessors[v] = u

		# Verificação da existência de círculos negativos
		for u in xrange(0, len(self.graph)):
			for v in xrange(0, len(self.graph)):
				if self.graph[u][v] == None:
					continue

				if self.distances[u] + self.graph[u][v] < self.distances[v]:
					raise NegativeWeightCycleError

		# lista de saída; índice -1 indica o custo total do menor caminho
		output = [ self.distances[destination] ]

		# Reconstruindo o menor caminho através do predecessor do destino
		while True:
			output.insert(0, destination)

			if destination == source:
				break
			else:
				destination = self.predecessors[destination]

		# Crianças, não façam isso em casa.
		return output[:-1], output[-1]

	def adjacencytListShortestPath(self, source, destination):
		'''
		Implementação através de lista de adjacência;

		Funcionalmente, o mesmo código acima. Porém, bem mais limpo e menos
		devorador de memória. Adequado para matrizes esparsas.
		'''
		
		source, destination = (self.graph.vertex[source],
								self.graph.vertex[destination])

		# A etapa de inicialização está parcialmente implícita no construtor
		# da classe Vertex. Assim, precisamos apenas atualizar o valor de
		# distância do nó origem.
		source.distance = 0

		for _ in self.graph.vertex:
			for e in self.graph.edges:
				if e.src.distance + e.wht < e.dst.distance:
					e.dst.distance = e.src.distance + e.wht
					e.dst.predescessor = e.src

		for e in self.graph.edges:
			if e.src.distance + e.wht < e.dst.distance:
				raise NegativeWeightCycleError

		output = [ destination.distance ]

		while True:
			output.insert(0, destination)

			if destination == source:
				break
			else:
				destination = destination.predescessor

		return output[:-1], output[-1]

'''
Matriz de adjacência; None pode ser utilizado para representar a inexistência
de arestas entre dois vértices.
'''
graph = [
	[7, 6, 8, 3, 5, 3, 2, 7, 1, 2, ],
	[0, 5, 2, 9, 1, 6, 2, 9, 9, 7, ],
	[6, 8, 7, 5, 8, 5, 7, 9, 8, 2, ],
	[6, 9, 7, 5, 8, 9, 8, 6, 3, 4, ],
	[0, 4, 8, 1, 6, 5, 8, 0, 7, 9, ],
	[2, 3, 3, 9, 9, 0, 0, 3, 0, 4, ],
	[7, 8, 0, 7, 7, 2, 9, 6, 0, 8, ],
	[3, 3, 5, 4, 8, 8, 8, 4, 4, 0, ],
	[9, 7, 2, 5, 0, 5, 4, 9, 0, 3, ],
	[6, 1, 8, 6, 6, 6, 1, 6, 7, 9, ],
]

# Calculando o menor caminho através da matriz
print BellmanFord(graph).adjacencyMatrixShortestPath(0,9)

# Calculando o menor caminho através da lista
print BellmanFord(Graph(graph)).adjacencytListShortestPath(0,9)
