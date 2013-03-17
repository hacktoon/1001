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
 	Dado uma conjunto de itens $I$ onde cada item $i$ possui um peso $p_i$ e um
	benefício $b_i$ associado, e uma mochila de carga máxima $m$, maximizar o
	benefício provido por uma combinação de itens respeitando a carga máxima
	suportda pela mochila. Em outras, palavras,
	satisfazer ao seguinte problema de otimização:
	%
	\begin{itemize}
		\item[] Maximizar $$\sum_{i=1}^{n} b_i x_i$$
		\item[] com a restrição $$\sum_{i=1}^{n} p_i x_i \le m$$
	\end{itemize}
	%
	onde $x_i$ é no número de repetiçoes do item $i$. A versão mais simples do
	problema, com cada item repetindo-se no máximo uma vez, ou $x_i \le 1$, é
	conhecida como 0-1 Knapsack. Instâncias sem essa limitação são conhecidas
	como Unbounded Knapsack.

    % OBS: a descrição acima é melhor visualizada após processada pelo LaTeX.
    % Visite http://scribtex.com/ para um compilador on-line

Complexidade:
	O(nm),	pseudo-polinomial no tempo, onde 'n' é cardinalidade do conjunto de
			item e 'm' é a carga máxima da mochila.

	O(nm),	pseudo-polinomial no espaço para o 0-1 Knapsack
	 O(m),	pseudo-polinomial no espaço para o Unbounded Knapsack

Dificuldade:
	Média

Referências:
	Robert Sdgewick. Algorithms in C. ISBN 0-201-51425-7
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
		'''
		Essa instância do problema da mochila possuí subestrutura ótima. Logo,
		é passível de resolução através de programação dinâmica. A seguinte
		formulação nos permite resolver esse problema numa abordagem bottom-up:

		% obs: LaTex code
		\[
			M[i,j] = \left\{
				\begin{array}{l l}
					M[i-1,j] & \text{se } p_i < j \\
					max(M[i-1,j], M[i,j-p_i] + b_i) & \text{se } p_i \ge j\\
				\end{array}
			\right.
		\]
		%
		Onde $M$ é uma matriz $n \times m$, $n$ é cardinalidade do conjunto
		de itens e $m$ a capacidade máxima da mochila.
		'''
		if not items:
			items = self.items

		M = [[ 0 ] * (self.maxWeight+1)]

		for i,item in enumerate(items, start=1):
			M.append([ 0 ] * (self.maxWeight+1))

			for w in xrange(1, self.maxWeight+1):
				if item.weight <= w:
					if M[i-1][w] > M[i-1][w-item.weight] + item.value:
						M[i][w] = M[i-1][w]
					else:
						M[i][w] = M[i-1][w-item.weight] + item.value
				else:
					M[i][w] = M[i-1][w]

		'''
		$M[n,m]$ nos informa o máximo benefício obtido. Porém, para recuperar
		a lista de itens escolhidos, Precisamos analisar a matriz $M$ mais a
		fundo.

		Caso o benefício da mochila com configuração $M[i,m]$ seja diferente do
		benefício da mochila com configuração $M[i-1,m]$, o item $i$ está entre
		os itens escolhidos. Assim, devemos continuar nossa busca na posição
		$M[i-1,m-p_i]$. Caso contrário, o item $i$ não está em nossa mochila e
		devemos continuar a busca na posição $M[i-1,m]$.

		O código abaixo o descrito acima.
		'''
		i,m = len(items), self.maxWeight
		output = [ ]

		while m > 0:
			if M[i][m] != M[i-1][m]:
				output.append(items[i-1])
				m = m - items[i-1].weight

			i = i - 1

		return M[-1][-1], output

	def unbounded(self, items=None):
		'''
		Essa instância do problema também possuí subestrutura ótima. Logo,
		também é passível de resolução através de programação dinâmica. A
		seguinte formulação nos permite resolver esse problema numa abordagem
		bottom-up:

		% obs: LaTex code
		$$ \displaystyle
		M[j] = max(M[j-1], ~\max_{\forall i \in I | p_i < j}(b_i + M[j-p_i]))
		$$
		%
		Onde $M$ é uma arranjo de cardinalidade $m$ e $m$ é a capacidade
		máxima da mochila.
		'''
		if not items:
			items = self.items

		M = [0] * (self.maxWeight+1)
		# Para que possamos recupera a lista de itens escolhidos, precisamos
		# de um arranjo auxiliar para armazenar a melhor escolha para a mochila
		# de tamanho 'j'.
		c = [None] * (self.maxWeight+1)

		for i,item in enumerate(items, start=1):
			for j in xrange(1, self.maxWeight+1):
				if item.weight <= j:
					if M[j] < M[j-item.weight] + item.value:
						M[j] = M[j-item.weight] + item.value
						c[j] = item

		'''
		Conceitualmente, $c[m]$ sempre está na mochila. Agora, para recuperar o
		restante dos itens, pasta decrementar m pelo peso do do item na posição
		em questão ($m = m - p_{c[m]}$)
		'''
		m = self.maxWeight
		output = [ ]

		while m > 0:
			output.append(c[m])
			m = m - c[m].weight

		return M[-1], output

items = [
	Item(15,2), Item(5,1), Item(20,3), Item(60,2)
]

k = Knapsack(6, items)

print k.zeroOne()
print k.unbounded()