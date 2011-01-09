#|
Calculo de media ponderada
Autor:
    ?
Colaborador:
    Daniel Valio    
Tipo:
    math
Descricao:
    Calcula a media ponderada entre tres numeros.
Complexidade:
    O(1)
Dificuldade:
    facil
|#

(defun media (a b c &optional (peso-a 1) (peso-b 1) (peso-c 1))
  (/ (+ (* a peso-a) (* b peso-b) (* c peso-c)) 
     (+ peso-a peso-b peso-c)))
