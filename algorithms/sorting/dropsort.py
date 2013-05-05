#!/usr/bin/env python2
# -*- coding: utf-8 -*- 
"""
Nome do algoritmo
Autor:
    David Morgan-Mar. <dmm@dangermouse.net>
Colaborador:
    Vinícius dos Santos Oliveira <vini.ipsmaker@gmail.com>
Tipo:
    sorting
Descrição:
    Dropsort é um algoritmo de ordernação lossy (causa perdas de informações)
    rápido, one-pass (lê a entrada exatamente uma vez, em ordem)

    O dropsort itera sobre os elementos da lista e, quando encontra um elemento
    menor que o anterior, descarta-o.
Complexidade:  
    O(n)
Dificuldade:
    facil
Referências:
    http://www.dangermouse.net/esoteric/dropsort.html
    http://students.cs.ndsu.nodak.edu/~abrjacks/dropsort.php (otimizações)
Licenca:
    MIT
"""

def dropsort(lst):
    i = 0
    prev = None
    while i != len(lst):
        if prev > lst[i]:
            del lst[i]
        else:
            prev = lst[i]
            i += 1

    return lst

if __name__ == '__main__':
    if dropsort([]) != []:
        exit(1)

    if dropsort([1, 2, 5, 3, 4, 6]) != [1, 2, 5, 6]:
        exit(1)

    if dropsort([1, 2, 2, 4]) != [1, 2, 2, 4]:
        exit(1)

    if dropsort([2, 11, 9, 8, 5, 4, 10, 3, 6, 0, 7, 13, 1, 12]) != [2, 11, 13]:
        exit(1)
