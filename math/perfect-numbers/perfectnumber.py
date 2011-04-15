# encoding: utf-8
""" 
Números perfeitos
Autor: 
      ?
Colaborador:
      Anna Cruz (anna.cruz@gmail.com)
Tipo:
    math, number-theory
Descrição:
    Esse algoritmo serve para verificar se um número é perfeito ou não. Números perfeitos são aqueles cuja soma dos divisores (exceto ele mesmo) é igual ao próprio número, como por exemplo 6, cujos divisores são 1, 2 e 3 e 1+2+3 = 6
Complexidade:
      ?
Dificuldade:
      fácil
Referências:
      http://en.wikipedia.org/wiki/Perfect_numbers
"""

def calc_perf(number):
  counter = 1
  divisors = []
  sumarize = 0
  while counter <= number/2:
    if number%counter == 0:
      divisors.append(counter)
    counter += 1
  for divisor in divisors:
    temp = divisor
    sumarize += divisor
  if sumarize == number:
    print "This is a perfect number"
  else:
    print "This is not a perfect number try again"

calc_perf(8128)
