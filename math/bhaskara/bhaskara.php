<?php
	
/*
Bhaskara
Autor: 
	Bhaskara Akaria [1]
Tipo: 
	math
Descriзгo: 
	Calcula as raнzes de uma equaзгo de segundo grau
Complexidade:
	Pior caso: O(1)
	Melhor caso: O(1)
Dificuldade:
	facil
Referкncias:
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