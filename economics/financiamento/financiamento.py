# -*- encoding: utf-8 -*-

"""
Financiamento
Autor:
    ?
Colaborador:
    Bruno Lara Tavares <bruno.exz@gmail.com>
Tipo:
    ?
Descrição:
	Calcula o valor das parcelas do financiamneto
	baseado no capital inicial e taxa de juros
	de acordo na função Price
Complexidade:
    ?
Dificuldade:
    facil
Referências:
    http://pt.wikipedia.org/wiki/Tabela_price#C.C3.A1lculo
"""

def parcelas(investimento, juros, periodo):
	return (investimento*juros) / (1 - (1/(1+juros)**periodo))
	
print parcelas(1000, 0.03, 4)
