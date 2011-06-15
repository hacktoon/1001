# encoding: utf-8

"""
Bozosort
Autor:
    Bozo
Colaborador:
    Karlisson Bezerra
Tipo:
    sorting
Descrição:
    Embaralha um vetor indefinidamente, até que os números estejam em ordem.
Complexidade:  
    O(infinito)
Dificuldade:
    facil
Referências:
    http://nerdson.com/blog/libbozo-01/
    http://pt.wikipedia.org/wiki/Bogosort
"""

from random import shuffle

def is_sorted(seq):
  # We define an empty sequence to be sorted by default.
  if not seq:
      return True

  # Otherwise, the sequence is sorted if every element is less or equal
  # than the next one.
  last = seq[0]
  for element in seq:
      if last > element:
          return False
      last = element
  return True

def bozosort(seq):
    while not is_sorted(seq):
        shuffle(seq)
    return seq

print bozosort([2,4,9,1,0,-4,17,8,0,23,67,-1])
