#|
Crivo de Eratostenes
Autor:
    Eratostenes de Cirene
Colaborador:
    Daniel Valio <valium97@mail.com>
Tipo:
    number-theory
Descricao:
    Encontra todos os primos entre dois nu'meros.
Complexidade:
    ?
Dificuldade:
    Facil/medio
|#

(defun primop (numero)
  (when (> numero 1)
    (loop for i from 2 to (isqrt numero) never (zerop (mod numero i)))))

(defun proximo-primo (numero)
  (loop for i from numero when (primop i) return i))

;;; Agora vem a parte magica.

(defmacro with-gensyms ((&rest names) &body body)
  `(let ,(loop for n in names collect `(,n (gensym)))
     ,@body))

;;; A macro do-primes aceita uma lista com nome de uma variavel, o limite inferior
;;; e o limite superior. Exemplo:
;;;
;;; (do-primes (alguma-var-inutil 0 100)
;;;   (print alguma-var-inutil))
;;;
;;; Esse exemplo retorna todos os primos de 0 a 100.

(defmacro do-primes ((var start end) &body body)
  (with-gensyms (ending-value-name)
    `(do ((,var (proximo-primo ,start) (proximo-primo (1+ ,var)))
	  (,ending-value-name ,end))
	  ((> ,var ,ending-value-name))
       ,@body)))

