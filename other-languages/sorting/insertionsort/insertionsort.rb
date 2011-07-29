# encoding: utf-8

=begin
Insertion Sort
Autor: 
    ?
Tipo:
    sorting
Colaborador:
    Bruno Lara Tavares <bruno.exz@gmail.com>
Descrição:
    Percorre uma lista da esquerda para direita e vai deixando os elementos
    mais a esquerda ordenados à medida que avança pela lista.
Complexidade:
    Pior caso: O(n²)
    Melhor caso: O(n)
Dificuldade:
    Facil
Referencia:
    http://pt.wikipedia.org/wiki/Insertion_sort
=end

class Array
    def insertion_sort!()
        (1..self.size-1).each do |i|
            elemento = self[i]
            j = i - 1

            while j >= 0 && self[j] > elemento
                self[j+1] = self[j]
                j -= 1
                self[j+1] = elemento
            end
        end
        self
    end
end

puts [5,6,8,1].insertion_sort!.inspect
