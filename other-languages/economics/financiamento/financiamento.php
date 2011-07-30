<?php
/**
Financiamento
Autor:
    Bruno Lara Tavares <bruno.exz@gmail.com>
Colaborador:
    Felipe Djinn <felipe@felipedjinn.com.br>
Tipo:
    econimics
Descrição:
	Calcula o valor das parcelas do financiamneto
	baseado no capital inicial e taxa de juros
	de acordo na função Price
Complexidade:
    ?
Dificuldade:
    facil
Referências:
    http://pt.wikipedia.org/wiki/Tabela_price#C.C3.A1lculo
*/
function financiamento($investimento, $juros, $periodo) {
    return ($investimento * $juros) / (1 - (1 / pow((1 + $juros), $periodo)));
}

echo financiamento(1000, 0.03, 4), "\n";
