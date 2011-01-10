#|
Fatorial
Autor
    ?
Colaborador
    Daniel Valio <valium97@mail.com>
Tipo
    math
Descricao
    Varias formas diferentes de se calcular um 
    fatorial em Common Lisp.
Complexidade
    (?)
Dificuldade
    Facil
|#

(defun fatorial-basico (n) ;;; Versao basica e recursiva
  (if (<= n 1)
      1
      (* n (fatorial-basico (- n 1)))))
(defun fatorial-melhorado (n &optional (acc 1)) ;;; Versao recursiva e (algo) otimizada
  (if (<= n 1)
      acc
      (fatorial-melhorado (- n 1) (* acc n))))
