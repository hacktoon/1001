#!/usr/bin/env python
# encoding: utf-8

'''
Insertion Sort
Autor: 
    ?
Tipo:
    sorting
Descrição:
    Percorre uma lista da esquerda para direita e vai deixando os elementos
    mais a esquerda ordenados à medida que avança pela lista.
Complexidade:
    Pior caso: O(n²)
    Melhor caso: O(n)
Dificuldade:
    Facil
Referencia:
    http://pt.wikipedia.org/wiki/Insertion_sort
'''

def insertion_sort(L):
    for i in range(1, len(L)):
        elemento = L[i]
        j = i - 1

        while j >= 0 and L[j] > elemento:
            L[j+1] = L[j]
            j -= 1
            L[j+1] = elemento

    return L
