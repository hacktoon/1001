<?php

/*
Bissexto
Autor:
    ?
Colaborador:
    Sérgio Mandrake <sergio_mandrake@yahoo.com.br>
Tipo:
    date
Descrição:
    Calcula os próximos anos bissextos
Complexidade:
    ?
Dificuldade:
    facil
Referências:
    http://pt.wikipedia.org/wiki/Ano_bissexto#Calend.C3.A1rio_Gregoriano
*/

function bissexto($numAnos = 4) {
    $anoAtual = $anoFinal = date('Y');
    $anoFinal += $numAnos;
    
    $anos = array();
    for ($i = $anoAtual; $i <= $anoFinal; $i++) {
        if ($i % 4 == 0 and ($i % 100 or $i % 400 == 0)) {
            $anos[] = $i;
        }
    }
    
    return $anos;
}

$proxAnosBissexto = bissexto(100);
echo join(', ', $proxAnosBissexto);
