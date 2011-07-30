# * encoding: UTF-8 *

"""
Divisors
Autor:
    ?
Colaborador:
    ?
Descricao:
   Mostra os divisores de um número
Complexidade:
    O(n)
Dificuldade:
    facil
"""

n = int(raw_input("Digite um numero: "))
for i in range(1, n+1):
    if not n % i:
        print i,
