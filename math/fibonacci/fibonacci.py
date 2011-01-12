# -*- encoding: utf-8 -*-
"""
 * Sequência de Fibonacci
 *
 * Autor:
 *   Felipe Djinn <felipe@felipedjinn.com.br>
 * Colaborador:
 *   Bruno Lara Tavares <bruno.exz@gmail.com>
 * Tipo:
 *   math
 * Descrição:
 *   Na matemática, os Números de Fibonacci são uma sequência definida como recursiva.
 *   O algoritmo recursivo que define a série aplica-se, na prática, conforme a regra sugere: 
 *   começa-se a série com 0 e 1; a seguir, obtém-se o próximo número de Fibonacci somando-se 
 *   os dois anteriores e, assim, sucessiva e infinitamente.
 * Complexidade:
 *   F(n) = {
 *      0 se n = 0;
 *      1 se n = 1;
 *      F(n - 1) + F(n - 2)
 *   }
 * Referências:
 *   http://pt.wikipedia.org/wiki/N%C3%BAmero_de_Fibonacci
 *
"""
def fibonacci(nesimo):
	if (nesimo < 2):
		return nesimo
	else:
		return fibonacci(nesimo - 1) + fibonacci(nesimo - 2)

for nesimo in range(20):
	print fibonacci(nesimo)
