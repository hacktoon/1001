<?php 

/*
Cсlculo da mщdia ponderada
Autor:
    ?
Colaborador:
    Karlisson Bezerra
Tipo:
    math
Descriчуo:
    Calcula a mщdia ponderada - щ um algoritmo
    comum em qualquer curso de introduчуo р programaчуo,
    que pode variar de acordo com os pesos.
Complexidade:  
    O(1)
Dificuldade:
    facil
*/

function media($n1, $n2, $n3) {
    $p1 = 4;
	$p2 = 5;
	$p3 = 6;
    return ($n1 * $p1 + $n2 * $p2 + $n3 * $p3) / ($p1 + $p2 + $p3);
}

print media(7.0, 8.0, 10.0);
?>