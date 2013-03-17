# coding: utf-8
"""
 * Sequência de Fibonacci
 *
 * Autor:
 *   Antonio Ribeiro <alvesjunior.antonio@gmail.com>
 * Tipo:
 *   math
 * Descrição:
 *   Na matemática, os Números de Fibonacci são uma sequência definida como recursiva.
 *   O algoritmo recursivo que define a série aplica-se, na prática, conforme a regra sugere: 
 *   começa-se a série com 0 e 1; a seguir, obtém-se o próximo número de Fibonacci somando-se 
 *   os dois anteriores e, assim, sucessiva e infinitamente.
 *
 *   Esta implementação baseia-se na propriedade de dividir-para-conquistar aplicada à
 *   potenciação de matrizes para acelerar o cálculo do número de fibonacci, reduzindo
 *   a complexidade do algoritmo para O(lg n)
 * Complexidade:
 *   O(lg n)
 * Dificuldade:
 *   Médio
 * Referências:
 *   http://assemblando.wordpress.com/2011/05/14/pela-uniao-dos-seus-poderes/
 *
"""

matriz_semente = [[1,1],[1,0]]

def pow_matriz(b,n):
    """Realiza a potenciação da matriz b pelo expoente n usando dividir-para-conquistar"""
    
    if n==1:
        return b

    if n%2:
        h = pow_matriz(b,(n-1)/2)
        return multi_matriz(multi_matriz(h,h),b)

    else:
        h = pow_matriz(b,n/2)
        return multi_matriz(h,h)


def multi_matriz(ma,mb):
    "Realiza a multiplicação de duas matrizes 2x2"

    (a,b),(c,d) = ma
    (e,f),(g,h) = mb
    return [[a*e+b*g,a*f+b*h],[c*e+d*g,c*f+d*h]]


def fibo(n):
    "Realiza (matriz_semente)^n e retorna o elemento da linha zero, coluna um"

    if n==0 or n==1:
        return n

    return pow_matriz(matriz_semente, n)[0][1]


if __name__=='__main__':
    for i in range(100):
        print fibo(i)
