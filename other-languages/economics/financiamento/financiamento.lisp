#|
Financiamento
Autor:
    ?
Colaborador:
    Daniel Valio <valium97@mail.com>
Tipo:
    economics
Descricao:
    Calcula o valor das parcelas do financiamento
    baseado no capital inicial e taxa de juros
    de acordo com a funcao Price
Complexidade:
    ?
Dificuldade:
    Facil
|#

(defun valor-parcela (capital juros periodo)
  (/ (* capital juros) (- 1 (/ 1 (expt (1+ juros) periodo)))))