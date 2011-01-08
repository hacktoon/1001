#|
Algoritmo de Euclides
Autor: Euclides de Alexandria
Tipo:  Teoria dos numeros
Desc.: Algoritmo de Euclides em sua forma moderna.
Complexidade: O(n^2) onde n e' o numero de digitos da entrada.
|#

(defun euclides (a b)
  (if (/= b 0)
      (euclides b (mod a b))
      a))