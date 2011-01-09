# encoding: utf-8

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


def fatorial(b):
	return 1 if b <= 1 else b*fatorial(b-1)

print fatorial(6)
