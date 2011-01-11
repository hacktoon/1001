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
    TODO: Fazer algo melhor que traduzir e exemplo em Clojure.
Complexidade
    ?
Dificuldade
    Facil
|#

(defun fibonacci (n)
  (if (< n 2)
      1
      (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))
