# -*- encoding: utf-8 -*-

=begin
Media Numerica
Autor:
    ?
Colaborador:
	Bruno Lara Tavares <bruno.exz@gmail.com>
    Guilherme Carlos (@guiessence)
Tipo:
    math
Descrição:
    Calcula a média de numeros inseridos pelo usuário
Complexidade:  
    0(1)
Dificuldade:
    facil
=end

def media(*args)
	sum = 0
	args.each do |i|
		sum += i
	end
	sum.to_f / args.size
end

#Adicione a quantidade de numeros que for preciso
puts media(2,3,4,10)
