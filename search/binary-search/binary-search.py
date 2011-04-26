# coding: utf-8
'''
Busca Binária

Autor: 
    	Jon Bentley
Colaborador:
    	Dayvid Victor (victor.dvro@gmail.com)
Tipo:
	search
Descrição: 
	Faz uma busca em um vetor ordenado, usando o recurso
	'dividir para conquistar'. Ele compara o valor a ser
	buscado com o centro do vetor, se for menor, o mesmo
	procedimento é feito com o sub-vetor da esquerda, se
	for maior, com o sub-vetor da direita.	
Complexidade de tempo: 
    O(log n)
Dificuldade: 
    fácil
Referências:
	http://pt.wikipedia.org/wiki/Pesquisa_binária
'''

def binary_search(value, l):
	if len(l) == 0:
		return -1
	mid = len(l)/2
	if value < l[mid]:
		return binary_search(value, l[:mid])
	elif value > l[mid]:
		tmp = binary_search(value, l[(mid + 1):])
		return (-1 if tmp == -1 else tmp + mid + 1)
	else:
		return mid

l = [0,1,2,3,4,7]
print binary_search(-1,l)
print binary_search(0,l)
print binary_search(1,l)
print binary_search(2,l)
print binary_search(3,l)
print binary_search(4,l)
print binary_search(5,l)
print binary_search(6,l)
print binary_search(7,l)
print binary_search(8,l)
print binary_search(9,l)







