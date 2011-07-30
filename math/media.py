# encoding: utf-8

"""
Cálculo da média ponderada
Autor:
    ?
Colaborador:
    Karlisson Bezerra
Tipo:
    math
Descrição:
    Calcula a média ponderada - é um algoritmo
    comum em qualquer curso de introdução à programação,
    que pode variar de acordo com os pesos.
Complexidade:  
    O(1)
Dificuldade:
    facil
"""

import math

def media(n1, n2, n3):
    p1, p2, p3 = 4, 5, 6
    return (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

print media(7.0, 8.0, 10.0)
