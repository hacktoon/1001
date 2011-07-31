# -*- coding: utf-8 -*-

"""
Sleepsort
Autor:
    ?
Colaborador:
    Saulo Andrade Almeida <sauloandrade@gmail.com>
Tipo:
    sorting
Descrição:
    Uma brincadeira sobre ordenacao numerica baseada em threads e sleep.
    O algoritimo dispara threads para cada numero que sera ordenado com o 
    tempo de espera baseado no valor do numero, ou seja quanto maior o 
    numero mais ele demora para acordar e ser reinserido na nova estrututa 
    ordenada.

    Para utilizar o algoritimo basta executar o arquivo e uma lista padrao 
    sera executado, ou informar um lista de valores separados por espacos.
    Ex: $ python sleepsort.py ou $ python sleepsort 4 7 3 9 8 1 2
Complexidade:  
    ?
Dificuldade:
    facil
Referências: (opcional)
    Adaptado de http://dis.4chan.org/read/prog/1295544154
"""

import sys, time, threading

def sleepit(val):
    time.sleep(val/4.0)
    print val

# se nao vier parametro, usa uma lista padrao
if not sys.argv[1:] :
    values = [7,9,2,5,6,4,1,8,3]

# se vier, usa a lisra informada
else:
    values = sys.argv[1:]

# loop que dispara as threads    
print "Ordenando a lista ", values
[ threading.Thread(target=sleepit, args=[int(a)]).start() for a in values ]
