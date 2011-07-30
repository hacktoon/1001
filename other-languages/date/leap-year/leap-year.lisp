#|
Bissexto
Autor:
    ?
Colaborador
    Daniel Valio <valium97@mail.com>
Tipo:
    date
Complexidade:
    O(1)
Dificuldade:
    Facil
|#

(defun ano-bissexto-p (&optional (ano (nth-value 5 (get-decoded-time))))
  (and (= (mod ano 4) 0) (or (/= (mod ano 100) 0) (= (mod ano 400) 0))))
  