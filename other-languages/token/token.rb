# -*- coding: UTF-8 -*-

=begin
Token

Autor:
    ?
Colaborador:
    Bruno Lara Tavares <bruno.exz@gmail.com>
    Felipe Djinn <felipe@felipedjinn.com.br>
Tipo:
    sequence
Descrição:
    Gera um token aleatório
Complexidade:
    ?
Dificuldade:
    facil
=end

def token(length = 10)
    rand(36**length).to_s 36
end


"""
Examples
"""

puts "Token com 10 caracteres (padrão): " + token()
puts "Token com 5 caracteres: " +token(5)
puts "Token com 15 caracteres " +token(15)
