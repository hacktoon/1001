# coding: utf-8
"""
Hamming Distance
Autor:
    Richard Hamming
Colaborador:
    Guido Luz Percú (guidopercu@gmail.com)
Tipo:
   edit-distance
Descrição:
    A distância de Hamming, é o número de posições em duas strings de mesmo
    tamanho onde os símbolos correspondentes são diferentes. Mede o mínimo
    número de substituições (ou o número de erros) necessárias para transformar
    uma string em outra.
Complexidade:
    ?
Dificuldade:
    facil
Referências:
    https://pt.wikipedia.org/wiki/Dist%C3%A2ncia_de_Hamming
    http://www.caip.rutgers.edu/~bushnell/dsdwebsite/hamming.pdf
Licenca:
    MIT
"""


def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


print(hamming_distance('ACGT', 'AGCT'))
