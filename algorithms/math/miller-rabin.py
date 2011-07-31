# -*- encoding: utf-8 -*-
"""
Teste de primalidade de Miller-Rabin
Autor:
    Gary L Miller e Michael O. Rabin
Colaborador:
    Juan Lopes (me@juanlopes.net)
Tipo:
    math
Descrição:
    Teste probabilistico de primalidade. Prova-se que para valores até 
    4.759.123.141, basta testar com as 'testemunhas' 2, 7 e 61. Este teste é 
    muito mais rápido do que testar através de 'trial division', principalmente 
    para números grandes.
Complexidade:  
    ?
Dificuldade:
    difícil
Referências: (opcional)
    http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
"""

def witness(a, n):
   u,t= (n/2, 1)
   while(u%2==0): 
      u,t = (u/2, t+1)
      
   prev = pow(a,u,n);
   
   for i in xrange(t):
      curr=(prev*prev)%n
      if curr==1 and prev!=1 and prev!=n-1: return True
      prev=curr
      
   return curr != 1
 
def is_prime(n):
   if n in (0, 1): return False
   if n in (2, 7, 61): return True
   if witness(2,n): return False
   if witness(7,n): return False
   if witness(61,n): return False
   return True
    
print 'Primos ate 20:'
for i in xrange(1, 20):
    if is_prime(i):
        print i

print '2 147 483 647?', is_prime(2147483647)
print '2 147 483 648?', is_prime(2147483648)
        
