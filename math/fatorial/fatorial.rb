# -*- encoding: utf-8 -*-

"""
Cálculo de fatorial
Autor:
    ?
Tipo:
    math
Descrição:
    Calcula o fatorial de um número
Complexidade:  
    Pior caso: ?
    Melhor caso: ?
Dificuldade:
    facil
"""


def fatorial(b)
	b <= 1 ? 1 : b*fatorial(b-1)
end

puts fatorial(6)
