#!/usr/bin/env python
# coding: utf-8

"""
Masochistic Sort
Author:
    Dilan Nery <dnerylopes AT gmail DOT com>
Colaborador:
    Dilan Nery <dnerylopes AT gmail DOT com>
Tipo:
    Ordenação
Descrição:
    Testa todas combinações possiveis de uma lista até encontrar a combinação
    em que a lista esteja ordenada
Complexidade:
    ?
Dificuldade:
    medio
Licensa:
    LGPL
"""

def masoquist_sort(L):
    if len(L) == 1:
        yield L
    elif len(L) == 2:
        count = 0
        while count < 2:
            L[0],L[1] = L[1],L[0]
            yield L
            count += 1
    else:
        for i in range(len(L)):
            L_copy = L[:]
            key = L_copy.pop(i)
            invert = masoquist_sort(L_copy)

            for i in invert:
                yield [key] + i
                
def is_sorted(L):
    flag = True
    for i in range(1,len(L)):
        if L[i-1] > L[i]:
            flag = False
    return flag                

if __name__ == '__main__':
    teste1 = masoquist_sort([2,4,1,5,4])
    for t1 in teste1:
        if is_sorted(t1):
            print t1
            break

    teste2 = masoquist_sort([2, 11, 9, 8, 5, 4, 10, 3, 6, 0, 7, 13, 1, 12])
    for t2 in teste2:
        if is_sorted(t2):
            print t2
            break
