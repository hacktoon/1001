# coding: utf-8
'''
Exponenciação
Autor: 
    	?
Colaborador:
    	Dayvid Victor (victor.dvro@gmail.com)
Tipo:
    	math
Descrição: 
	calcula exponenciação
Complexidade de tempo: 
    	O(log n)
Dificuldade: 
    	fácil
Referências:
	?
'''
def pow(x, n):
	if n < 0:
		return float(1) / float(pow(x, -n))
	p = (pow(x, n/2) if n != 0 else 1)
	return (p * p if n % 2 == 0 else p * p * x)

print [pow(2,n) for n in range(11)]
print [pow(2,n) for n in range(-11,0)]



