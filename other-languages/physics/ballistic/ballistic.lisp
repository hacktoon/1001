#|
Balistica
Autor:
    ?
Colaborador:
    Daniel Valio <valium97@mail.com>
Tipo:
    physics
Complexidade:
    O(1)
Dificuldade:
    Facil
|#

(defun backend-tiro (vetor-horizontal vetor-vertical gravidade 
		     &optional (x 0) (y 0) (time 0) (angulo 0))
  (if (> y 0)
      (backend-tiro vetor-horizontal vetor-vertical 
		    gravidade (* time vetor-horizontal)
		    (- (+ y (* time vetor-vertical))
		       (* gravidade (expt time 2)))
		    (1+ time))
      (list angulo x y)))
(defun simula-tiro (angulo forca gravidade y)
  (backend-tiro (* forca (cos angulo))
		(* forca (sin angulo))
		gravidade 0 y 0 angulo))