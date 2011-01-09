# encoding: utf-8

"""
Bhaskara
Autor:
    Bhaskara Akaria [1]
Colaborador:
    Karlisson Bezerra
Tipo:
    math
Descrição:
    Calcula as raízes de uma equação de segundo grau
Complexidade:  
    O(1)
DIficuldade:
    facil
Referências:
    [1] http://pt.wikipedia.org/wiki/Bhaskara_Akaria
"""

import math

def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None
    else:
        raizes = []
        m1 = math.sqrt(delta)
        r1 =(-b + m1) / (2 * a)
        raizes.append(r1)
        r2 =(-b - m1) / (2 * a)
        raizes.append(r2)
        return raizes

print(bhaskara(1, -1, -2))
