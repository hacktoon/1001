#!/usr/bin/env python3.1

"""
ROT13
Autor:
    ?
Colaborador:
    Fernando Medeiros <fekomedeiros - at - gmail.com>
Tipo:
    sequence
Descrição: 
    Implementação do algoritmo ROT-13, ou "Rotate By 13".
    É um procedimento simples mas eficaz para garantir que textos eletrônicos 
    não sejam lidos por distração ou acidente.
    Util para proteger mensagens que talvez o leitor não queira ler. 
    Exemplo, "spoilers" sobre determinado assunto em Fóruns ou listas de discussão.
Complexidade:
    ?
Dificuldade:
    facil
Referências:
    http://pt.wikipedia.org/wiki/ROT13
"""

def rot13(text):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    rotated = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    r13 = "".maketrans(alpha, rotated)
    return text.translate(r13)

#Exemplos de uso:

print(rot13("Agora estou usando ROT-13!"))
#Exibe a mensagem: Ntben rfgbh hfnaqb EBG-13!

print(rot13("Ntben rfgbh hfnaqb EBG-13!"))
#Exibe a mensagem: Agora estou usando ROT-13!
#Note que a mesma função é usada para codificar e decodificar o texto.
