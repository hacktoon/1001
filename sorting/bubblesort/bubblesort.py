# encoding: utf-8

"""
Bubblesort
Autor:
    ?
Tipo:
    sorting
Descrição:
    Varre o vetor comparando cada um dos pares de números
    possíveis e trocando suas posições no vetor se necessário
Complexidade:  
    Pior caso: O(n²)
    Melhor caso: O(n²)
Dificuldade:
    facil
Referências:
    http://en.wikipedia.org/wiki/Bubble_sort
"""

def bubble(lst):
    for i, val1 in enumerate(lst):
        for j, val2 in enumerate(lst):
            if lst[i] < lst[j]:
               lst[i], lst[j] = lst[j], lst[i]
    return lst

print bubble([6, -7, 1, 12, 9, 3, 5])
