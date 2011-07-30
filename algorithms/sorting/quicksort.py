# coding: utf-8
"""
Quicksort
Autor:
    C.A.R. Hoare
Colaborador:
    Adriano Melo (adriano@adrianomelo.com)
Tipo:
    sorting
Descrição:
    Quicksort é um algorítmo de ordenação de vetores cuja estratégia é
    dividir para conquistar. Basicamente o algorítmo organiza os elementos
    dos vetores de forma que os menores estejam antes dos maiores.
    Esse passo é feito recursivamente até que a lista completa esteja ordenada.
Complexidade:  
    O(n log(n)) - Melhor caso e médio caso.
    O(n²) - Pior caso.
Dificuldade:
    facil
Referências: (opcional)
    http://pt.wikipedia.org/wiki/Quicksort
"""
from random import randint

def quicksort (array):
	if len(array) <= 1:
		return array

	pivot   = array.pop()
	
	smaller = []
	equal   = [pivot]
	larger  = []

	for ele in array:
		if ele < pivot:
			smaller.append(ele)
		elif ele > pivot:
			larger.append(ele)
		else:
			equal.append(ele)

	return quicksort(smaller) + equal + quicksort(larger)

print quicksort([i for i in xrange(30)]) # worst case
print quicksort([3 for i in xrange(30)]) # best case
print quicksort([randint(-100, 400) for i in xrange(30)]) # average case

