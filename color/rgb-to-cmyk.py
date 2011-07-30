# encoding: utf-8

'''
RGB to CMYK
Autor:
    ?
Colaborador:
    Aurélio A. Heckert
Tipo:
    color
Descrição:
    Converte uma cor definida em RGB para CMYK.

    RGB é um sistema aditivo de definição de cores, representa a mistura de luz. Suas componentes são (em ordem) vermelho, verde e azul.
    CMYK é um sistema subtrativo de definição de cores, representa a mistura de pigmentos. Suas componentes são (em ordem) ciano, magenta, amarelo e preto. O preto no CMYK deriva uma necessidade do uso prático, já que a mistura dos 3 pigmentos é custoso, não é realmente preto e a sobreposição de impressões tornaria o desalinhamento mais perceptível nos detalhes escuros.
    O algorítimo deste exemplo considera as componentes como valores flutuantes entre 0 e 1, onde 0 significa sem representação e 1 máxima representação. Sendo assim o branco seria (1,1,1) em RGB e (0,0,0,0) em CMYK, o vermelho intenso seria (1,0,0) em RGB e (0,1,1,0) em CMYK e o laranja seria (1,0.5,0) em RGB e (0,0.5,1,0) em CMYK. A representação das componentes em valores flutuantes entre 0 e 1 pode parecer estranho pelo nosso costume em ver cores definidas com 1 byte por unidade, mas essa representação é bastante útil em vários algorítimos para manipulação de cores e ainda viabiliza representações com maior profundidades de cores (mais de 1 byte por componente).
Complexidade:  
    O(1)
DIficuldade:
    facil
Referências:
    http://en.wikipedia.org/wiki/RGB
    http://en.wikipedia.org/wiki/CMYK
'''

def rgb2cmyk( red, green, blue ):

    black = min( 1-red, 1-green, 1-blue )
    nb = 1 - black  # negative black
    if black == 1:
        cyan    = 0
        magenta = 0
        yellow  = 0
    elif nb > 0:
        cyan    = ( nb - red   ) / nb
        magenta = ( nb - green ) / nb
        yellow  = ( nb - blue  ) / nb
    else:
        cyan    = 1 - red
        magenta = 1 - green
        yellow  = 1 - blue

    return "%.1f  %.1f  %.1f  %.1f" % ( cyan, magenta, yellow, black )


print 'Preto:\t\t\t',       rgb2cmyk( 0.0, 0.0, 0.0 )
print 'Cinza escuro:\t\t',  rgb2cmyk( 0.3, 0.3, 0.3 )
print 'Cinza médio:\t\t',   rgb2cmyk( 0.5, 0.5, 0.5 )
print 'Cinza claro:\t\t',   rgb2cmyk( 0.7, 0.7, 0.7 )
print 'Branco:\t\t\t',      rgb2cmyk( 1.0, 1.0, 1.0 )
print 'Vermelho vivo:\t\t', rgb2cmyk( 1.0, 0.0, 0.0 )
print 'Vermelho sangue:\t', rgb2cmyk( 0.7, 0.0, 0.0 )
print 'Laranja:\t\t',       rgb2cmyk( 1.0, 0.5, 0.0 )
print 'Verde Musgo:\t\t',   rgb2cmyk( 0.6, 0.7, 0.6 )
