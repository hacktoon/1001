# coding: utf-8
'''
Exponenciação Modular
Autor: 
    ?
Colaborador:
    Juan Lopes <me@juanlopes.net>
Tipo:
    math
Descrição: 
    Calcula exponenciação modular de inteiros em tempo logaritmico.
        
    Baseia-se no fato de que:
    (a*b)%n == ((a%n) * (b%n)) % n
Complexidade de tempo: 
    O(log n)
Dificuldade: 
    fácil
Referências:
    ?
'''
def pow(x, e, m):
    if e==0: return 1
    p = pow(x,e/2,m)%m
    k = (1 if e%2==0 else x)
    return (p*p*k)%m

for i in range(20):
    print '3 ^ %d mod 1000 = %d (%d)' % (i, pow(3, i, 1000), 3**i)



