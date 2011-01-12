# -*- encoding: utf-8 -*-
=begin
Haversine
Autor:
    ?
Colaborador:
    Bruno Lara Tavares <bruno.exz . at . gmail . com>
Tipo:
    geography
Descrição:
    Calcula a distancia mais curta
    entre dois pontos com latitude e longitude
    na superficie da Terra
    usando a formula de haversine
Complexidade:
    ?
Dificuldade:
    medio
Referências:
    http://en.wikipedia.org/wiki/Haversine_formula

=end

class String	
	def Todegree
	    grau, minuto, segundo = self.split().collect {|i| i.to_f}
	    if(self.include? "-")
	        grau -= (minuto/60) + (segundo/3600)
	    else
	        grau += (minuto/60) + (segundo/3600)
            end
	end
end

class Numeric
	def degrees
	    self * Math::PI / 180.0
	end
end

def haversin(theta)
	Math.sin(theta/2)**2
end

Radius = 6371 
def distancia(latitude1, longitude1, latitude2, longitude2)
	deltaLatitude = (latitude2 - latitude1).degrees
	deltaLongitude = (longitude2 - longitude1).degrees
	h = haversin(deltaLatitude) + Math.cos(latitude1.degrees)*Math.cos(latitude2.degrees )*haversin(deltaLongitude)
	2*Radius*Math.asin(Math.sqrt(h))
end

puts distancia("53 08 50".Todegree,"-01 50 58".Todegree,"52 12 16".Todegree,"00 08 26".Todegree)
