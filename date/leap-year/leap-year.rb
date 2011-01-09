=begin

Bissexto
Autor:
    ?
Colaborador:
    Bruno Lara Tavares <bruno.exz . at . gmail . com>
Tipo:
    date
Descrição:
    Calcula os próximos anos bissextos
Complexidade:
    ?
Dificuldade:
    facil
Referências:
    http://pt.wikipedia.org/wiki/Ano_bissexto#Calend.C3.A1rio_Gregoriano

=end

def anoBissexto(anos)
	anoAtual = Time.now.year
	proximoAno = anoAtual + anos
	bissextos = []
	(anoAtual..proximoAno).each do |ano|
		if (ano%4 == 0) && (ano % 100 != 0 || ano % 400 == 0)
			bissextos << ano
		end
	end
	bissextos
end

puts anoBissexto(100)

