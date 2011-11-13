# -*- encoding: utf-8 -*-

"""
Media Numerica
Autor:
    ?
Colaborador:
	Bruno Lara Tavares <bruno.exz@gmail.com>
    Guilherme Carlos (@guiessence)
Tipo:
    math
Descrição:
    Calcula a média de numeros inseridos pelo usuário
Complexidade:  
    0(1)
Dificuldade:
    facil
"""

from __future__ import division

def media(*args):
	sum = 0
	for i in args:
		sum += i
	return sum / len(args)

#Adicione a quantidade de numeros que for preciso
print media(2,3,4,10)
