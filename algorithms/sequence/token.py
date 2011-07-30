#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Token

Autor:
    ?
Colaborador:
    Felipe Djinn <felipe@felipedjinn.com.br>
Tipo:
    sequence
Descrição:
    Gera um token aleatório
Complexidade:
    ?
Dificuldade:
    facil
"""

import random
import string

def token(length = 10):
 return ''.join(random.choice(string.letters) for i in xrange(length)) 


"""
Examples
"""

print "Token com 10 caracteres (padrão): " + token()
print "Token com 5 caracteres: " +token(5)
print "Token com 15 caracteres " +token(15)
