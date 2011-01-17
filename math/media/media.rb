# encoding: utf-8

=begin
Cálculo da média ponderada
Autor:
    ?
Colaborador:
    Bruno Lara Tavares <bruno.exz@gmail.com>
    Karlisson Bezerra
Tipo:
    math
Descrição:
    Calcula a média ponderada - é um algoritmo
    comum em qualquer curso de introdução à programação,
    que pode variar de acordo com os pesos.
Complexidade:  
    O(1)
Dificuldade:
    facil
=end


def media(n1, n2, n3)
    p1, p2, p3 = 4, 5, 6
    (n1 * p1 + n2 * p2 + n3 * p3).to_f / (p1 + p2 + p3)
end

puts media(7.0, 8.0, 10.0)
