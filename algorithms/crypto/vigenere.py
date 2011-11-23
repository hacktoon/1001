#!usr/bin/python
# encoding: utf-8

"""
Vigenère cipher (Cifra de Vigenère)
Autor:
  Giovan Battista Bellaso (1553) "La cifra del. Sig. Giovan Battista Bellaso"
  Foi erradamente atribuida a Blaise de Vigenère
Colaborador:
  damor - dave-world (at) hotmail.com
Tipo:
  Crypto
Descrição:
  Este algoritmo implementa o metodo de criptografia "Cifra de Vigenère"
  "A cifra de Vigenère consiste no uso de várias cifras de César em sequência,
  com diferentes valores de deslocamento ditados por uma "palavra-chave"" - Wiki
Complexidade:
  ?
Dificuldade:
  facil
Referências: (opcional)
  http://pt.wikipedia.org/wiki/Cifra_de_Vigen%C3%A8re
Licenca:(opcional)
  GPL
"""

class Vigenere(object):
  def __init__(self):
    self.tabulaRecta = [ [ 0 for i in range(26) ] for j in range(26) ] # Construir a tabula recta (Grelha de Vigenere)
    for i in range(26):
      for j in range(26):
        ch = ord("A")+j+i
        if (ch>90): ch-=26
        self.tabulaRecta[i][j] = chr(ch)

  def crypt(self, plaintext = "", chave= ""):
    self.newKey=chave
    while len(self.newKey)<len(plaintext): self.newKey+=chave
    chave = self.newKey[:len(plaintext)]
    pos = 0
    cipher = ""
    for c in plaintext:
      cipher += self.tabulaRecta[ord(chave[pos]) % 26][ord(c) % 26]
      pos += 1
    return cipher

  def decrypt(self, ciphertext = "", chave=""):
    self.newKey=chave
    while len(self.newKey)<len(ciphertext): self.newKey+=chave
    chave = self.newKey[:len(ciphertext)]
    cipher = ""
    iter = 0
    for c in chave:
      pos = 0
      for k in range(26):
        if (self.tabulaRecta[ord(c)-ord("A")][k] == ciphertext[iter]):
          cipher += chr(ord("A")+pos)
        pos += 1
      iter += 1
    return cipher

v = Vigenere()
encWord = v.crypt("ATACARBASESUL","LIMAO")
print encWord
print v.decrypt(encWord,"LIMAO")
