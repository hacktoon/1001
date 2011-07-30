#|
Calculo da sequencia de Fibonacci
Autor
    ?
Colaborador
    Daniel Valio <valium97@mail.com>
Tipo
    math
Descricao
    Calculo de Fn aonde F e' a sequencia de Fibonacci.
    Note-se que, apesar de ser quase o mesmo co'digo
    da versao em Clojure, esta e' muito mais ra'pida,
    pois em Common Lisp ha' TCO (Tail Call Optimization).
Complexidade
    ?
Dificuldade
    Facil
|#

(defun fibonacci (n)
  (if (< n 2)
      1
      (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))
