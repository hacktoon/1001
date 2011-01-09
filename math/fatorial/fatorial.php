<?php 
/*
Cálculo de fatorial
Autor:
    ?
Colaborador:
    ?
Tipo:
    math
Descrição:
    Calcula o fatorial de um número
Complexidade:  
    ?
Dificuldade:
    facil
*/


function fatorial($b) {
	return $b <= 1 ? 1 : $b*fatorial($b-1);
}

echo fatorial(6);

?>
