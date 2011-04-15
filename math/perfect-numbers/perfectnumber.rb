# encoding: utf-8

=begin
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
=end


def calc_perf(number)
  counter  = 1
  divisors = []
  sumarize = 0
  while counter <= number/2 do
    divisors.push(counter) unless number%counter != 0
    counter += 1
  end
  sum = divisors.inject(:+)
  if sum == number 
    puts "This is a perfect number" 
  else
    puts "This is not a perfect number"
  end
end

calc_perf(8128)
