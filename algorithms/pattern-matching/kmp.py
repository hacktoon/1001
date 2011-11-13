# -*- encoding: utf-8 -*-
"""
KMP (Knuth-Morris-Pratt) algorithm
Autor:
    Donald Knuth, Vaughan Pratt and James H. Morris
Colaborador:
    Juan Lopes (me@juanlopes.net)
Tipo:
    pattern-matching
Descrição:
    Encontra todas as instâncias de P em Q em tempo linear.
    Usa tabela de lookup inicializada por P.
Complexidade:  
    O(n+m)
Dificuldade:
    Médio
Referências: (opcional)
    http://en.wikipedia.org/wiki/KMP_algorithm
"""

def kmp_init(P):
    F = [0]*(len(P)+1)
    i, j= 1, 0;
    while i<len(P):
        if P[i] == P[j]: 
            i+=1; j+=1; F[i] = j
        elif j == 0: 
            i+=1; F[i] = 0;
        else:            
            j = F[j];
    return F
    
def kmp(Q, P):
    F = kmp_init(P)
   
    i,j,n,m = 0,0,len(Q),len(P)
    
    while i-j <= n-m:
        while j < m:
            if P[j] == Q[i]: i+=1; j+=1
            else: break
        
        if j == m: yield i-m;
        elif j == 0: i+=1;
        j = F[j];


print list(kmp("casacasacasa", "casa")) #0, 4, 8
print list(kmp("cacacacacaca", "caca")) #0, 2, 4, 6, 8