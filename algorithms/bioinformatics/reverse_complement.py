# coding: utf-8
"""
Reverse Complement
Autor:

Colaborador:
    Guido Luz Percú (guidopercu@gmail.com)
Tipo:
   bioinformatics
Descrição:
    Converte uma sequência de DNA em seu complemento, isto é, inverte a string e troca A por T, T por A, C por G e G por C.
Complexidade:
    ?
Dificuldade:
    facil
Licenca:
    MIT
"""


def reverse_complement(genoma):
    dicionario = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complemento_reverso = [dicionario[x] for x in genoma[::-1]]
    return "".join(complemento_reverso)

print(reverse_complement('ATCG')) # CGAT
