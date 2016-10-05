# encoding: utf-8

"""
Permutation
Autor:
    Fabian Stedma
Colaborador:
    Bruno Gabriel dos Santos (bruno.gsantos89@gmail.com)
Tipo:
    math
Descrição:
    Calcula o número de combinações distintas que são possíveis de serem formadas por um array numérico.
Complexidade:  
    O(n!)
Dificuldade:
    medio
Referências: 
    [1] https://en.wikipedia.org/wiki/Permutation#Algorithms_to_generate_permutations
"""

def permutation(input_data, temp_data, position):
	if position == len(input_data):
		print ''.join(str(temp_data))
	else:
		for i in xrange(len(input_data)):
			is_same = False
			for j in xrange(position):
				if temp_data[j] == input_data[i]:
					is_same = True
			if not is_same:
				if len(temp_data) <= i:
					temp_data.append(input_data[i])
				else:
					temp_data[position] = input_data[i]
				permutation(input_data, temp_data, position+1)

permutation([1,2,3], [], 0)

