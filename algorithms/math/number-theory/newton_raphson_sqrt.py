# -*- encoding: utf-8 -*-
"""
Cálculo da raíz quadrada através do método de Newton-Raphson
Autor:
     Isaac Newton e Joseph Raphson
Colaborador:
    Alysson Oliveira (lssn.oliveira@gmail.com)
Tipo:
    math
Descrição:
    Método interativo para estimar as raízes de funções e pode ser aplicado
    a para o cálculo de rais quadrada.
Complexidade:
    ?
Dificuldade:
    fácil
Referências: (opcional)
    https://pt.wikipedia.org/wiki/M%C3%A9todo_de_Newton-Raphson
    https://courses.csail.mit.edu/6.006/fall11/rec/rec12_newton.pdf
    http://www.iaps.org.in/journal/index.php/journaliaps/article/view/161/146
    Guttag, John V. Introduction to Computation and Programming Using \
    Python. MIT Press. 2013. ISBN 978-0-262-52500-8
"""


def newton_raphson_sqrt(n, precisao=0.001, debug=False):
    """
    n: Valor que se deseja obter a raíz
    precisao: Valor de precisão (ex.: 0.01)
    debug: Quando True mostra os chutes até que a precisão seja satisfeita
    """
    chute = 0.5 * n
    while abs(chute * chute - n) >= precisao:
        if debug:
            print('    Chute:', chute)
        chute = chute - (((chute**2) - n) / (2 * chute))
    return chute


# Testando a função
for i in 49, 64:
    print('Calculando raíz de {}'.format(i))
    print('Resultado: {}'.format(newton_raphson_sqrt(i)))
    print(35 * '=')


for i in 81, 100:
    print('Calculando raíz de {}'.format(i))
    print('Resultado: {}'.format(newton_raphson_sqrt(i, 0.01, True)))
    print(35 * '=')
