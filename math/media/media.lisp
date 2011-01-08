#|
Calculo de media ponderada
Autor: Desconhecido
Tipo:  Matematica
Desc.: Calcula a media ponderada entre tres numeros.
Complexidade: O(1)
|#

(defun media (a b c &optional (peso-a 1) (peso-b 1) (peso-c 1))
  (/ (+ (* a peso-a) (* b peso-b) (* c peso-c)) 
     (+ peso-a peso-b peso-c)))