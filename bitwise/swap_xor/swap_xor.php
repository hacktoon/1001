<?php
/*
Algoritimo de troca de variáveis
Autor:
    ?
Colaborador:
    José Ivan Bezerra Vilarouca Filho (ivanfilho2204@hotmail.com)
Tipo:
    bitwise
Descrição:
    Algoritimo que tem objetivo de trocar os valores
	de duas variáveis sem o uso de uma variável temporária
	usando apenas o operdador boolean "ou exclusivo".
	Lembrando que esse algorítimo só funciona se as variáveis
	tiverem em locais diferentes na memória
Complexidade:
    O(1)
Dificuldade:
    fácil
Referências:
	http://en.wikipedia.org/wiki/XOR_swap_algorithm
*/

function swap(&$a, &$b) {

	$a = $a ^ $b;
	$b = $a ^ $b;
	$a = $a ^ $b;
}

$var1 = 1991;
$var2 = 1989;

echo "Valores antes da troca: \$var1=$var1 \$var2=$var2<br />";
swap($var1, $var2);
echo "Valores despois da troca: \$var1=$var1 \$var2=$var2<br />";
?>