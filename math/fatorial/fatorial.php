<?php 
/*
Cálculo de fatorial
Autor:
    ?
Tipo:
    math
Descrição:
    Calcula o fatorial de um número
Complexidade:  
    Pior caso: ?
    Melhor caso: ?
Dificuldade:
    facil
*/


function fatorial($b) {
	return $b <= 1 ? 1 : $b*fatorial($b-1);
}

echo fatorial(6);

?>
