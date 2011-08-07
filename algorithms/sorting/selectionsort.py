# encoding: utf-8
'''
Insertion Sort
Autor:
    ?
Colaborador:
	Bruno Coimbra <bbcoimbra@gmail.com>
Tipo:
    sorting
Descrição:
	Percorre uma lista a procura do menor valor e inclui na posição correta.
Complexidade:
	O(n²)
Dificuldade:
    Facil
Referencia:
    http://pt.wikipedia.org/wiki/Selection_sort
'''
from random import randint

def selectionsort(L):
	for i in range(0, len(L)):
		minor = L[i]
		minor_pos = i
		for j in range(i+1, len(L)):
			if L[j] < minor:
				minor = L[j]
				minor_pos = j
		L[i], L[minor_pos] = minor, L[i]
	return L

A = [randint(1, 50) for i in range(30)]
print A
print selectionsort(A)

