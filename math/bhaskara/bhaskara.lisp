#|
Formula de Bhaskara 
Autor:
    Bhaskara Akaria
Tipo:
    math
Descricao:
    Calcula as raizes de uma equacao de segundo grau 
Complexidade:
    O(1)
Dificuldade:
    facil
|#

(defun delta-calc (a b c)
  (- (expt b 2) (* a c 4)))
(defun achar-raizes (a b delta)
  (list (/ (- delta b) (* a 2))
	(/ (- (+ delta b)) (* a 2))))
(defun bhaskara (a b c)
  (unless (< (delta-calc a b c) 0)
    (achar-raizes a b (delta-calc a b c))))
