# -*- encoding: utf-8 -*-
"""
 * Sequência de Fibonacci
 *
 * Autor:
 *   Felipe Djinn <felipe@felipedjinn.com.br>
 * Colaborador:
 *   Bruno Lara Tavares <bruno.exz@gmail.com>
 *   Dilan Nery <dnerylopes@gmail.com>
 * Tipo:
 *   math
 * Descrição:
 *   Na matemática, os Números de Fibonacci são uma sequência definida como recursiva.
 *   O algoritmo recursivo que define a série aplica-se, na prática, conforme a regra sugere: 
 *   começa-se a série com 0 e 1; a seguir, obtém-se o próximo número de Fibonacci somando-se 
 *   os dois anteriores e, assim, sucessiva e infinitamente.
 * Complexidade:
 *   O(n)
 * Referências:
 *   http://pt.wikipedia.org/wiki/N%C3%BAmero_de_Fibonacci
 *
"""
def fibonacci(nesimo):
    c, n1, n2 = 0, 0, 1
    while c < nesimo:
        n1, n2 = n2, n1 + n2
        c += 1
    return n2

for nesimo in range(100):
	print fibonacci(nesimo)
