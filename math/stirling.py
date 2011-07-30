# -*- encoding: utf-8 -*-
"""
 Fórmula de Stirling

 Autor:
   Pedro Menezes <eu@pedromenezes.com>
   DiogoK <diogo@diogok.net>
 Tipo:
   math
 Descrição:
   A Fórmula de Stirling estabelece uma aproximação assintótica para o fatorial de um número.
 Referências:
   http://pt.wikipedia.org/wiki/F%C3%B3rmula_de_Stirling
"""

from math import sqrt, pi, e, pow

def stirling(n):
    return sqrt(2*pi*n) * pow(n/e, n)

if __name__ == '__main__':
    for n in xrange(1, 10):
        print("fat %d ~ %f" %(n, stirling(n)))