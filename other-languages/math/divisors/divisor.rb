# * encoding: UTF-8 *

=begin
Divisors
Autor:
    ?
Colaborador:
    Bruno Lara Tavares <bruno.exz@gmail.com>
Descricao:
   Mostra os divisores de um número
Complexidade:
    O(n)
Dificuldade:
    facil
=end


class Numeric
    def divisores()
        a = []
        (1..self+1).each do |i|
            if self % i == 0
                a.push i
            end
        end
        a
    end
end

puts 12.divisores.inspect
