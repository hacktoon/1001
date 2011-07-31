# coding: utf-8
'''
Distância Levenshtein
Autor:
    Vladimir Levenshtein (1965)
Colaborador:
    Flávio Juvenal da Silva Junior (flaviojuvenal@gmail.com)
Descricao:
    A distância Levenshtein ou distância de edição entre duas strings
    é dada pelo número mínimo de operações necessárias para transformar
    uma string na outra. Entendemos por operações a inserção, deleção ou
    substituição de um caractere. Dessa forma, essa distância mede a
    quantidade de diferença entre duas strings (quanto maior, mais diferentes).
    E por isso é útil para aplicações de casamento de padrões, como
    corretores ortográficos.
Complexidade:
    O(len(s) * len(t)), onde s e t são as strings
Dificuldade:
    médio
Referências:
    http://en.wikipedia.org/wiki/Levenshtein_distance
    http://www.csse.monash.edu.au/~lloyd/tildeAlgDS/Dynamic/Edit/
Licenca:
    MIT
'''

def levenshtein(s, t):
    '''
    Implementação da versão não-recursiva do algoritmo.
    Veja em: http://en.wikipedia.org/wiki/Levenshtein_distance#Computing_Levenshtein_distance
    Observação: os -1 nas linhas 49 e 60 são porque em Python os índices
    das listas começam em 0.
    '''
    m = len(s) + 1
    n = len(t) + 1
    from_0_to_m = range(m)
    from_0_to_n = range(n)
    d = [[0]*n for _ in from_0_to_m]
    
    for i in from_0_to_m:
	d[i][0] = i
    for j in from_0_to_n:
	d[0][j] = j
    
    from_1_to_m = from_0_to_m[1:]
    from_1_to_n = from_0_to_n[1:]
    for j in from_1_to_n:
	for i in from_1_to_m:
	    if s[i-1] == t[j-1]:
		d[i][j] = d[i-1][j-1] #nenhuma operação necessária
	    else:
		d[i][j] = min(
		    d[i-1][j] + 1,   #uma exclusão
		    d[i][j-1] + 1,   #uma inserção
		    d[i-1][j-1] + 1, #uma substituição
		)
    return d[m-1][n-1]

if __name__ == '__main__':
    s = "kitten"
    t = "sitting"
    result = levenshtein(s, t)
    expected_result = 3
    #3, já que deve trocar k por s, e por i e inserir g
    assert result == expected_result
    print result
