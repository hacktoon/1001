# -*- encoding: utf-8 -*-
"""
Bissexto
Autor:
    Bruno Lara Tavares <bruno.exz . at . gmail . com>
Tipo:
    date
Descrição:
    Calcula os próximos anos bissextos
Complexidade:
    Pior caso: ?
    Melhor caso: ?
Dificuldade:
    facil
Referências:
    http://pt.wikipedia.org/wiki/Ano_bissexto#Calend.C3.A1rio_Gregoriano

"""

from datetime import datetime

def anoBissexto(anos):
	anoAtual = datetime.now().year
	proximoAno = anoAtual + anos
	for ano in range(anoAtual,proximoAno):
		if !(ano % 4):
			yield ano

for ano in anoBissexto(20): print ano
