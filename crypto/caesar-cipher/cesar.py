#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Cesar Cipher (Cifra de César)
Autor:
    César
Colaborador:
    Apu, Sigano, InFog, Paulo, Doug, ExHora <gccsd@lista.gccsd.com.br>
Tipo:
    crypto
Descrição:
    Este algoritmo implementa a Cifra de César
    Este algoritmo foi implementado em um Dojo do Grupo de Compartilhamento do
    Conhecimento Santos Dumont <http://gccsd.com.br>
Complexidade:  
    ?
Dificuldade:
    facil
Referências:
    http://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar
Licenca:
    GPL
"""

__authors__ = (
    "Apu",
    "Sigano",
    "InFog",
    "Paulo",
    "Doug",
    "ExHora"
)

import string

class Cesar(object): 
    
    def __init__(self):
        self.INICIO = 65
        self.FIM = 90
        self.ESPACO = 32
    
    def crypt(self, entrada = "", chave = 0):
        saida = ""
        entrada = entrada.upper()

        for letra in entrada:
            valor = ord(letra)
            
            if (not valor == self.ESPACO):
                valor += chave
                if (valor > self.FIM):
                    valor -= 26
            saida += chr(valor)
            
        return saida
    
    def decrypt(self, entrada = "", chave = 0):
        saida = ""
        entrada = entrada.upper()
        
        for letra in entrada:
            valor = ord(letra)
            
            if (not valor == self.ESPACO):
                valor -= chave
                if (valor < self.INICIO):
                    valor += 26
            saida += chr(valor)
        
        return saida

c = Cesar()
print c.crypt("a ligeira raposa marrom saltou sobre o cachorro cansado", 3)
print c.decrypt("D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR", 3)
