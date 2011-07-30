# coding: utf-8
'''
Array Sum
Autor:
    ?
Colaborador:
    Dayvid Victor (victor.dvro@gmail.com)
Descricao:
    Esse programa recebe como parametro uma lista
    e retorna a soma dos elementos desta lista.
Complexidade:
    O(n)
Dificuldade:
    facil
Licenca:
    GPL
'''

def arraysum(l, key = lambda a, b: a + b):
	s = 0
	for e in l:
		s = key(s,e)
	return s

if __name__ == '__main__':
	l1 = [1,2,3,4,5,6,7,8,9,10]
	l2 = [-4,-3,-2,-1,0,1,2,3,4]

	print arraysum(l1)
	print arraysum(l2)

