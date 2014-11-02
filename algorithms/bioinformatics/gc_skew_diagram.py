# coding: utf-8
"""
Skew Diagram
Autor:

Colaborador:
    Guido Luz Percú (guidopercu@gmail.com)
Tipo:
   bioinformatics
Descrição:
    Monta os pontos de um diagrama GC Skew, um diagrama que mostra a diferença entre G (guanina) e C (citosina) em um DNA.
Complexidade:
    ?
Dificuldade:
    facil
Referências:
    https://en.wikipedia.org/wiki/GC_skew
Licenca:
    MIT
"""

def gc_skew_diagram(genome):
    qtd_c = 0
    qtd_g = 0
    skew = [0]
    for base in genome:
        if base == 'C':
            qtd_c += 1
        elif base == 'G':
            qtd_g += 1
        skew.append(qtd_g - qtd_c)
    return skew

print(gc_skew_diagram('ACCCCGTACTGGGGG'))
