# coding: utf-8
"""
Transcrição
Autor:

Colaborador:
    Guido Luz Percú (guidopercu@gmail.com)
Tipo:
   bioinformatics
Descrição:
    Transcrição é o processo de formação do RNAm mensageiro a partir da cadeia-molde de DNA
Complexidade:
    ?
Dificuldade:
    facil
Referências:
    https://pt.wikipedia.org/wiki/Transcri%C3%A7%C3%A3o_%28gen%C3%A9tica%29
Licenca:
    MIT
"""
def transcrever(dna):
  """ Transforma string DNA em string RNAm """
  return dna.replace('T', 'U')

print(transcrever('ACGT'))
