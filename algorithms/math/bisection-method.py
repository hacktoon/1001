# encoding: utf-8
"""
Método da Bisseção
Autor:
    ?
Colaborador:
    Lucas Andrade (lucasfael@gmail.com)
Tipo:
    math
Descrição:
    Calcula a raiz aproximada de uma equação polinomial qualquer
    dentro de um intervalo até uma precisão desejada.
Complexidade:  
    O(log n)
Dificuldade:
    facil
Referências:
    http://www.im.ufrj.br/dmm/projeto/projetoc/precalculo/sala/conteudo/capitulos/cap114.html
    
"""

import math

def root(function, x0, x1, precision=0.0001):
    x0 *= 1.0
    x1 *= 1.0
    while (math.fabs(x0-x1) > precision):
        fx0 = function(x0)
        fx1 = function(x1)
        if (fx0 * fx1) > 0:
            return
        if fx0 == 0:
            return x0
        if fx1 == 0:
            return x1
        x2 = (x0 + x1) / 2
        fx2 = function(x2)
        if (fx0 * fx2) < 0:
            x1 = x2
        else:
            x0 = x2
    return x0

def funcao(x):
    return math.pow(x, 3)-(9 * x) + 3

x = root (funcao, 0, 1)
print x
