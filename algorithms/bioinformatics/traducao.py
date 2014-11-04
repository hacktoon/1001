# coding: utf-8
"""
Tradução
Autor:

Colaborador:
    Guido Luz Percú (guidopercu@gmail.com)
Tipo:
   bioinformatics
Descrição:

Complexidade:
    ?
Dificuldade:
    facil
Referências:
    https://pt.wikipedia.org/wiki/Tradu%C3%A7%C3%A3o_%28gen%C3%A9tica%29
    https://en.wikipedia.org/wiki/Genetic_code
Licenca:
    MIT
"""


def traducao(rna):
    assert len(rna) % 3 == 0
    resultado = ''
    codigo_genetico = {
        'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V', 'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUA': 'L',
        'CUA': 'L', 'AUA': 'I', 'GUA': 'V', 'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V', 'UCU': 'S', 'CCU': 'P',
        'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'UCA': 'S', 'CCA': 'P', 'ACA': 'T',
        'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
        'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'UAA': '', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'UAG': '',
        'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R',
        'AGC': 'S', 'GGC': 'G', 'UGA': '', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W', 'CGG': 'R', 'AGG': 'R',
        'GGG': 'G',
    }
    for i in range(0, len(rna), 3):
        traducao = codigo_genetico[rna[i:i+3]]
        if traducao != '':
            resultado +=traducao
    return resultado
print(traducao('ACGUUA'))
