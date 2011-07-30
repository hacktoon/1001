# -*- encoding: utf-8 -*-
=begin
 * Sequência de Fibonacci
 *
 * Autor:
 *   Felipe Djinn <felipe@felipedjinn.com.br>
 * Colaborador:
 *   Bruno Lara Tavares <bruno.exz@gmail.com>
 * Tipo:
 *   math
 * Descrição:
 *   Na matemática, os Números de Fibonacci são uma sequência definida como recursiva.
 *   O algoritmo recursivo que define a série aplica-se, na prática, conforme a regra sugere: 
 *   começa-se a série com 0 e 1; a seguir, obtém-se o próximo número de Fibonacci somando-se 
 *   os dois anteriores e, assim, sucessiva e infinitamente.
 * Complexidade:
 *   F(n) = {
 *      0 se n = 0;
 *      1 se n = 1;
 *      F(n - 1) + F(n - 2)
 *   }
 * Referências:
 *   http://pt.wikipedia.org/wiki/N%C3%BAmero_de_Fibonacci
 *
=end
class Numeric
	def fibonacci
		if (self < 2)
			self
		else
			(self - 1).fibonacci + (self -2).fibonacci
		end
	end
end

(0..20).each do |nesimo|
	puts nesimo.fibonacci
end
