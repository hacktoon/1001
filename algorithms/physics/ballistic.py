#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Balistica
Autor:
    ?
Colaborador:    
    GabrielBap <gabrielbap1@gmail.com>
Tipo:
    physics
Descrição:
    Informa a distância horizontal quem um projétil atingiu baseado na força aplicada, força da gravidade e ângulo da força.
Complexidade:
    0(1)
Dificuldade:
    facil
Referências:
    [1]http://www.algosobre.com.br/fisica/balistica-e-lancamento-de-projetil.html
"""

from math import pi, sin, cos, radians

def simula_tiro(angle, forca, gravidade, startY):
   
   angleR = radians(angle) # As funções sin e cos trabalham com radianos
   
   time = 0 # tempo inicial do tiro
   # Define os vetores de força vertical e horizontal
   VetorVertical = sin(angleR) * forca
   VetorHorizontal = cos(angleR) * forca
   # Pow!
   Y = startY
   X = 0
   while Y > 0: # Enquanto a bala não cair...
      X = VetorHorizontal * time # Distância atual em X (S = V * t)
      Y = startY + (VetorVertical * time) - (gravidade * (time**2)) # Distância atual em Y (S = S0 + V*t + (a * t^2)/2)
      time += 1
   
   return angle, X, Y

forca = float(raw_input("Qual será a força? "))
gravidade = float(raw_input("Qual será a força da gravidade? "))
startY = float(raw_input("Qual será a altura do canhão? "))
try:
   angle = float(raw_input("Qual será o ângulo? (Opcional) "))
   dados = simula_tiro(angle, forca, gravidade, startY)
   resultado = "Ângulo = %i\n X = %.5f\n Y = %.5f\n\n" % (dados[0], dados[1], dados[2])
   print resultado
except:  
   for angle in range(0,91): # Faz a simulação em todos os ângulos de 0 a 90
      dados = simula_tiro(angle, forca, gravidade, startY)
      resultado = "\nÂngulo = %i\nX = %.5f\nY = %.5f\n" % (dados[0], dados[1], dados[2])
      print resultado
