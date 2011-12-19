# -*- coding: utf-8 -*-

"""
Algoritmo de Aho-Corasick.

Autor:
	Alfred Aho and Margaret Corasick (1975)

Colaborador:
	Pedro Arthur Duarte (JEdi)
	pedroarthur.jedi@gmail.com

Tipo:
	multi pattern string matching
	finite automate-based

Descrição:
	Dado um conjunto de padrões, esse algoritmo constrói uma máquina de estados
	finitos de forma que seja possível buscá-los no texto de entrada em tempo
	linearmente proporcional ao tamanho dessa última. Para isso, o algoritmo de
	Aho-Corasick utiliza uma estrutura de dados semelhante as Tries, porém com
	nós adicionais que evitam a necessidade de backtracking. Esse nós
	adicionais representam o maior prefixo comum presente entre os padrões.

Complexidade:
	O(⅀m) de pré-processamento, onde "m" é o tamanho do padrão
	O(n)  de busca, onde "n" é o tamanho do texto de entrada

Dificuldade:
  média (?)

Referências:
  https://en.wikipedia.org/wiki/Aho-Corasick_algorithm

Licença:
  GPLv3

"""

class AhoCoraski(dict):
	failTransition = None
	isTerminal = False

	def __init__(self, patternList=None, thenBuild=False):
		if patternList is not None:
			self.add(patternList)

		if thenBuild is True:
			self.build()

	def add(self, pattern):
		if isinstance(pattern, list):
			for w in pattern:
				self.add(w)

			return self

		currentState = self

		for c in pattern:
			if c not in currentState:
				currentState[c] = AhoCoraski()

			currentState = currentState[c]

		currentState.isTerminal = pattern

		return self

	def build(self):
		queue = [ self ]

		while len(queue) > 0:
			current = queue.pop(0)

			for transition, next in current.iteritems():
				state = current.failTransition

				while state is not None and transition not in state:
					state = state.failTransition

				if state is not None:
					next.failTransition = state[transition]
				else:
					next.failTransition = self

				queue.append(next)

		return self

	def match(self, subject):
		output = [ ]
		current = self

		if isinstance(subject, list):
			for s in subject:
				output += self.match(s)

			return output

		for c in subject:
			if c in current:
				current = current[c]
			else:
				current = current.failTransition

				while current is not None and c not in current:
					current = current.failTransition

				if current is not None:
					current = current[c]
				else:
					current = self

			if current.isTerminal is not False:
				output.append(current.isTerminal)

		return output

patternList = [ 'he', 'she', 'his', 'her', 'show', 'shall', 'hall', ]

print AhoCoraski(patternList, True).match("This phrase shall match")
