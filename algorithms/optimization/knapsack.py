# -*- coding: utf-8 -*-

"""
Algoritmo da Mochila

Autor:

Colaborador:
	Pedro Arthur Duarte (JEdi)
	pedroarthur.jedi@gmail.com

Tipo:
	0-1 Knapsack Problem
	Unbounded Knapsack
	Dynamic Programming

Descrição:
	Dado uma conjunto de itens $I$ onde cada item $i$ possui um peso $p$ e um
	benefício $b$ associado, e uma mochila de carga máxima $m$, maximizar o
	benefício provido por uma combinação de itens. Em outras, palavras,
	satisfazer ao seguinte problema de otimização:
	%
	\begin{itemize}
		\item[] maximizar $\sum^{i=1}_{n} b_i x_i$,
		\item[] com a restrição $\sum^{i=1}_{n} p_i x_i \le m$
	\end{itemize}
	%
	onde $x_i$ é no número de repetiçoes do item $i$. A versão mais simples do problema, com cada item repetindo-se no máximo uma vez, ou $x_i \le 1$, é conhecida como 0-1 Knapsack. Instâncias sem essa limitação são conhecidas
	como Unbounded Knapsack.

    OBS: a descrição acima é melhor visualizada após processada pelo LaTeX.
    Visite http://scribtex.com/ para um compilador on-line

Complexidade:
	O(nm),	pseudo-polinomial no tempo, onde n é cardinalidade do conjunto de
			item em é a carga máxima da mochila.

	O(nm),	pseudo-polinomial no espaço para o 0-1 Knapsack
	 O(m),	pseudo-polinomial no espaço para o Unbounded Knapsack

Dificuldade:
	Médio

Referências:
	https://secure.wikimedia.org/wikipedia/en/wiki/Knapsack_problem

Licença:
	GPLv3

"""

class Item:
	def __init__(self, value, weight, label=None):
		self.value = value
		self.weight = weight

		if label == None:
			self.label = str((self.value, self.weight))
		else:
			self.label = label

	def __repr__(self):
		return '<Item ' + self.label + '>'

class Knapsack:
	def __init__(self, maxWeight, items=None):
		self.maxWeight = maxWeight
		self.items = items

	def zeroOne(self, items=None):
		if not items:
			items = self.items

		m = [[ 0 ] * (self.maxWeight+1)]

		for i,item in enumerate(items, start=1):
			m.append([ 0 ] * (self.maxWeight+1))

			for w in xrange(1, self.maxWeight+1):
				if item.weight <= w:
					if m[i-1][w] > m[i-1][w-item.weight] + item.value:
						m[i][w] = m[i-1][w]
					else:
						m[i][w] = m[i-1][w-item.weight] + item.value
				else:
					m[i][w] = m[i-1][w]

		n,w = len(items), self.maxWeight
		output = [ m[n][w] ]

		while n > 0 and w > 0:
			if m[n][w] != m[n-1][w]:
				output.append(items[n-1])
				w = w - items[n-1].weight

			n = n - 1

		return output[0], output[1:]

	def unbounded(self, items=None):
		if not items:
			items = self.items

		m = [0] * (self.maxWeight+1)
		c = [None] * (self.maxWeight+1)

		for i,item in enumerate(items, start=1):
			for j in xrange(1, self.maxWeight+1):
				if item.weight <= j:
					if m[j] < m[j-item.weight] + item.value:
						m[j] = m[j-item.weight] + item.value
						c[j] = item

		n = self.maxWeight
		output = [ ]

		while n > 0:
			output.append(c[n])
			n = n - c[n].weight

		return m[-1], output

items = [
	Item(15,2), Item(5,1), Item(20,3), Item(60,2)
]

k = Knapsack(6, items)

print k.zeroOne()
print k.unbounded()