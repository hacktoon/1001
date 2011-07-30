# -*- coding: utf-8 -*-

"""
Algoritmo de Edmonds-Karp.

Autor:
  Jack Edmonds & Richard Karp (1972)

Colaborador:
  Pedro Arthur Duarte (JEdi)
  pedroarthur.jedi@gmail.com

Tipo:
  graph

Descrição:
  O Algoritmo de Edmonds-Karp é uma implementação do método de Ford-Fulkerson
  para o cálculo do fluxo máximo em uma rede de fluxos. Esse algoritmo é
  idêntico ao método de Ford-Fulkerson excetuando-se no critério que utiliza
  para a escolha do caminho aumentante: o caminho precisa ser o menor caminho
  que possibilita o aumento do fluxo.

Complexidade:
  O(V*E²),  onde 'V' é a cardinalidade o conjunto de vértices e 'E' a
            cardinalidade do conjunto de arestas.

Dificuldade:
  alta (?)

Referências:
  http://en.wikipedia.org/wiki/Edmonds

Licença:
  GPLv3

"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from sys import stdin;

DIMACS = 0
WFLOW = 1
RAW = 2

IMPERATIVE = 0
FUNCTIONAL = 1

class EdmondsKarp:
  # Cria nova instância da classe.
  # Parâmetros:
  #   c: matriz de fluxos (f[i,j] = c[i][j])
  #   s: vértice do qual se origina o fluxo;
  #   t: vértice de destino do fluxo;
  def __init__(self, c, s, t):
    self.c = c
    self.s = s
    self.t = t

    # Matriz auxiliar dos fluxos
    self.f = [[0] * len(i) for i in c]

    #print c

  # Iterador para auxiliar na construção da resposta
  def __iter__(self):
    return self

  # Busca primeiro em largura:
  def next(self):
    q = [ self.s ]
    p = { self.s: [] }

    # Critério: capacidade(e) - fluxoatual(e) > 0

    # Implementação imperativa (aquela que se encontra geralmente nos livros)
    if self.approach == IMPERATIVE:
      for u in q:
        for v in xrange(len(self.c)):
          if self.c[u][v] - self.f[u][v] > 0 and v not in p:
            p[v] = p[u] + [(u,v)]
            if v == self.t:
              return p[v]
            q.append(v)

    # Implementação por meio de diretivas funcionais. Bonito, mas impraticável
    # para grandes instâncias desse problema.
    else:
      fcond = (lambda x: x[0][1] - x[1] > 0 and x[0][0] not in p)
      for u in q:
        for v in map(
                  lambda x: x[0][0],
                  filter(fcond, zip(enumerate(self.c[u]), self.f[u]))):
          p[v] = p[u] + [(u,v)]
          if v == self.t:
            return p[v]
          q.append(v)

    raise StopIteration

  # Esse algoritmo também é capaz de determinar o corte mínimo.
  # Esse método faz isso :-)
  def MinCutVertex(self):
    q = [ self.s ]
    o = [ ]

    for u in q:
      for v in xrange(len(self.c)):
        if self.c[u][v] - self.f[u][v] > 0 and v not in o:
          o.append(v)
          q.append(v)

    return o

  # Retorna a matriz de fluxos
  def FlowEdges(self, outtype=RAW):
    # Retorna a própria matriz de fluxos
    if outtype == RAW:
      return self

    # seleciona apenas os vértices que possuem algum fluxo
    if outtype == WFLOW:
      q = [ self.s ]
      p = []
      u = 0

      fcond =

      for u in q:
        f = map(
              lambda x: x[0][0],
              filter(
                   lambda x:x[1]>0 and (u,x[0][0],self.f[u][x[0][0]]) not in p,
                   zip(enumerate(self.c[u]), self.f[u])
              )
        )
        for v in f:
          p = p + [(u,v,self.f[u][v])]
          q.append(v)

      return p

    # retorna nada =p
    else:
      return [ ]

  # Implementação do algoritmo de Edmonds-Karp
  def MaxFlow(self, approach=IMPERATIVE):
    self.approach = approach

    # Enquanto houverem caminhos aumentantes,
    # selecione aquele de menor custo;
    for p in self:

      # Dentro desse caminho, encontre a aresta
      # que possuí menor capacidade de vazão:
      mf = min(map(lambda e: self.c[e[0]][e[1]] - self.f[e[0]][e[1]], p))

      # Ajuste os valores da matriz de fluxo de
      # acordo com o vazão da aresta encontrada
      # no passo anterior
      for u,v in p:
        self.f[u][v] += mf
        self.f[v][u] -= mf

    # Retorna o fluxo máximo
    return sum(self.f[self.s])

