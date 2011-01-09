#|
Algoritmo de Euclides
Autor:
    Euclides de Alexandria
Colaborador:
    Daniel Valio
Tipo:
    number-theory
Descricao:
    Algoritmo de Euclides em sua forma moderna.
Complexidade:
    O(n^2) onde n e' o numero de digitos da entrada.
Dificuldade:
    facil
|#

(defun euclides (a b)
  (if (/= b 0)
      (euclides b (mod a b))
      a))
