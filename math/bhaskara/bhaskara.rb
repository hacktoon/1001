# encoding: utf-8

=begin
Bhaskara
Autor:
    Bhaskara Akaria [1]
Colaborador:
	Bruno Lara Tavares <bruno.exz@gmail.com>
    Karlisson Bezerra
Tipo:
    math
Descrição:
    Calcula as raízes de uma equação de segundo grau
Complexidade:  
    O(1)
DIficuldade:
    facil
Referências:
    [1] http://pt.wikipedia.org/wiki/Bhaskara_Akaria
=end

def bhaskara(a, b, c)
    delta = b ** 2 - 4 * a * c
    if delta < 0
        nil
    else
        raizes = []
        m1 = Math.sqrt delta
        r1 =(-b + m1) / (2 * a)
        raizes.push r1
        r2 =(-b - m1) / (2 * a)
        raizes.push r2
    end
end
puts bhaskara 1, -1, -2
