# coding: utf-8
'''
Hamming Distance
Autor:
	Hamming
Colaborador:
	Adriano Melo <adriano@adrianomelo.com>
	Dayvid Victor <victor.dvro@gmail.com>
Tipo:
	artificial-intelligence
Descrição:
	Algorítmo para calcular a distância entre vetores com dados categóricos.
Complexidade:  
	O(n) - sendo n o tamanho do vetor
Dificuldade:
	fácil
Referências:

'''

def hamming(a, b):
	return sum([hamming_i(ai, bi) for ai, bi in zip(a,b)])

def hamming_i(ai, bi):
	return (0 if ai == bi else 1)

def knn(k, treino, padrao, distancia=lambda a,b: sum([(c-d)**2 for c,d in zip(a,b)])):
	k_nearest = sorted([[distancia(pe[:-1], padrao), pe[-1]] for pe in treino])[:k]
	return max(set([e[-1] for e in k_nearest]), key = [e[-1] for e in k_nearest].count)



if __name__ == '__main__':
	train = [['gordo', 'baixo', 'devagar', 'golfista'],
		['magro', 'alto', 'rapido', 'jogador de basquete'],
		['magro', 'baixo','rapido', 'jogador de futebol'],
		['gordo', 'alto', 'rapido', 'jogador de futebol americano'],
		['medio', 'medio', 'rapido', 'jogador de tenis']]
	
	padrao = ['magro', 'medio', 'rapido']
	
	print knn(1, train, padrao, distancia = hamming)

