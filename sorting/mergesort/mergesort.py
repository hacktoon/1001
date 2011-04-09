"""
Mergesort
Autor:
	John von Neumann, em 1945
Colaborador:
	Adriano Melo (adriano@adrianomelo.com)
Tipo:
	sorting
Descrição:
	O algoritmo ordena um vetor dividindo-o pela metade e, depois de processar
	cada metade recursivamente, intercala as metades ordenadas.
Complexidade:
	O (n*log(n))
Dificuldade:
	fácil
Referências:
	?
"""

def intercala (inicio, fim):
	minimo = min(len(inicio), len(fim))
	result = []
	i, j   = 0, 0

	while i < minimo and j < minimo:
		if inicio[i] < fim[j]:
			result.append(inicio[i])
			i = i + 1

		elif inicio[i] >= fim[j]:
			result.append(fim[j])
			j = j + 1

	result = result + inicio[i:]
	result = result + fim [j:]
	
	return result

def mergesort(array):
	tamanho = len(array)

	if tamanho == 1:
		return array

	inicio = mergesort (array[0:tamanho/2])
	fim    = mergesort (array[tamanho/2:])

	return intercala (inicio, fim)

print mergesort ([2,8,-2,1,45,37,-463,24,50,80,4,3,7,4,55])

