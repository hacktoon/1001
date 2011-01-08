#|
Bozosort (a.k.a Bogosort)
Autor: Bozo
Tipo:  Ordenacao de vetores
Descricao: Embaralha um vetor indefinidamente, ate' que os numeros estejam em ordem.
Complexidede: Pior caso: O(infinito)
              Melhor caso: O(n)

PS: Essa versao trabalha com listas, e nao vetores de fato.
|#

(defun shuffle-list (l)
  (loop for i below (length l) do
       (rotatef
	 (elt l i)
	  (elt l (random (length l)))))
  l)
(defun bozosort (lista)
  (if (equalp lista (sort lista #'<))
      lista
      (bozosort (shuffle-list lista))))