# coding: utf-8
'''
Algorítimo de Luhn
Autor:
    Hans Peter Luhn
Colaborador:
    Alberto Chvaicer <achvaicer@gmail.com>
Tipo:
    math
Descrição:
    Algoritimo utilizado para calular o dígito verificador baseado no módulo de 10. Utilizado por cartões de crédito e número IMEI.
Complexidade de tempo:
    O(n)
Dificuldade:
    media
Referências:
    https://en.wikipedia.org/wiki/Luhn_algorithm
'''
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def calculate_luhn(partial_card_number):
    check_digit = luhn_checksum(int(partial_card_number) * 10)
    return check_digit if check_digit == 0 else 10 - check_digit

print 'the check digit of 7992739871 is %d' % (calculate_luhn(7992739871)) # should be 3
