# -*- encoding: utf-8 -*-
"""
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

"""
from __future__ import division
import math


def strTodegree(string):
    grau, minuto, segundo = [int(x) for x in string.split()]
    if(string.find("-") == -1):
        grau += (minuto/60) + (segundo/3600)
    else:
        grau -= (minuto/60) + (segundo/3600)
    return grau


def haversin(theta):
	return math.sin(theta/2)**2


def distancia(latitude1, longitude1, latitude2, longitude2):
	Radius = 6371 #Terra
	deltaLatitude = math.radians(latitude2 - latitude1)
	deltaLongitude = math.radians(longitude2 - longitude1)
	h = haversin(deltaLatitude) + math.cos(math.radians(latitude1))*math.cos(math.radians(latitude2))*haversin(deltaLongitude)
	return 2*Radius*math.asin(math.sqrt(h))

print distancia(strTodegree("53 08 50"),strTodegree("-01 50 58"),strTodegree("52 12 16"),strTodegree("00 08 26"))
