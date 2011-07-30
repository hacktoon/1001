# -*- encoding: utf-8 -*-

"""
Cálculo de fatorial
Autor:
    ?
Colaborador:
    Bruno Lara Tavares <bruno.exz@gmail.com>
Tipo:
    math
Descrição:
    Calcula o fatorial de um número
Complexidade:  
    ?
Dificuldade:
    facil
"""


def fatorial(b)
	b <= 1 ? 1 : b*fatorial(b-1)
end

puts fatorial(6)
