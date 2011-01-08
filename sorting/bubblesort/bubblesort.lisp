#|
Bubble sort
Autor: Desconhecido
Tipo:  Ordenacao de vetores
Descricao: Compara elementos dois a dois e checa se estao na ordem correta.
Complexidade: Pior caso: O(n^2)
            Melhor caso: O(n)
|#

(defun bubble-sort (array)
  (let ((result (copy-seq array)))
    (loop for i from (1- (length result)) downto 0 do
        (loop for j from 0 to i
            when (< (aref result i) (aref result j))
               do (rotatef (aref result i) (aref result j))))
    result))

