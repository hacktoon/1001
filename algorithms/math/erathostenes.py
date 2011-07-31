# -*- encoding: utf-8 -*-
"""
Crivo de Eratóstenes
Autor:
    Eratóstenes de Cirene
Colaborador:
    Juan Lopes (me@juanlopes.net)
Tipo:
    Exemplos: math
Descrição:
    Gera array de primalidade de inteiros através de algoritmo com baixa 
    complexidade.
Complexidade:  
    O(n loglogn)
Dificuldade:
    Médio
Referências: (opcional)
    http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

from math import sqrt

def sieve(n):
    P = [True]*n
    P[0] = False
    P[1] = False
    
    for i in xrange(2, int(sqrt(n))):
        if P[i]:
            for j in xrange(i**2, n, i):
                P[j] = False
    return P

def primes_up_to(n):
    for i, p in enumerate(sieve(n)):
        if p: 
            yield i
    
print 'Primos ate 20:'
for i in primes_up_to(20):
    print i

