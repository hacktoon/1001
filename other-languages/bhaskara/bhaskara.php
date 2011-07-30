<?php
	
/*
Bhaskara
Autor: 
	Bhaskara Akaria [1]
Colaborador:
    ?
Tipo: 
	math
Descrição: 
	Calcula as raízes de uma equação de segundo grau
Complexidade:
	O(1)
Dificuldade:
	facil
Referências:
	[1] http://pt.wikipedia.org/wiki/Bhaskara_Akaria
*/

	function bhaskara($a, $b, $c) {
		$delta = ($b * $b)  - (4 * $a * $c);
		if($delta < 0) 
			return null;
		else {
			$raizes = "";
			$m1 = sqrt($delta);
			$r1 = (-$b + $m1) / (2 * $a);
			$raizes[] = $r1;
			$r2 =(-$b - $m1) / (2 * $a);
			$raizes[] = $r2;
			return $raizes;
		}
		
	}
	
	// Passando um array com valores a serem ordenados
	print_r(bhaskara(1, -1, -2))
	
?>
