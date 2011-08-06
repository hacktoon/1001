# encoding: utf-8

"""
Bozo factoring
Autor:
    Ricardo Bittencourt
Colaborador:
    Ricardo Bittencourt (bluepenguin@gmail.com)
Tipo:
    number-theory
Descrição:
    Calcula os fatores primos de um numero usando o pior algoritmo conhecido.
Complexidade:  
    O(n^n)
Dificuldade:
    medio
Referências:
    http://blog.ricbit.com/2010/07/o-algoritmo-mais-lento-do-oeste.html
Licenca:
    GPL
"""

import itertools

def factor(n):
  solutions = []
  for f in itertools.product(range(1,1+n),repeat=n):
    if reduce(lambda x,y: x*y, f) == n:
      solutions.append(filter(lambda x:x>1, list(f)))
  solutions.sort(key=len, reverse=True)
  return solutions[0]

print factor(6)
