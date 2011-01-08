<?php
	
/*
Bubblesort
Autor: 
	?
Tipo: 
	sorting
Descriчуo: 
	Varre o vetor comparando cada um dos pares de nњmeros
	possэveis e trocando suas posiчѕes no vetor se necessсrio
Complexidade:
	Pior caso: O(nВ)
	Melhor caso: O(n)
Dificuldade:
	facil
Referъncias:
	http://en.wikipedia.org/wiki/Bubble_sort
*/

	function bubble($valores) {
		$ordenado = false;
		$certo = $valores;
		sort($certo);
		
		for($i=0;$i<count($valores);$i++) {
			for($x=0;$x<count($valores);$x++) {
				if($valores[$i] < $valores[$x]) {
					$tmp = $valores[$i];
					$valores[$i] = $valores[$x];
					$valores[$x] = $tmp;
				}
			}
		}
		
		return $valores;
		
	}
	
	// Passando um array com valores a serem ordenados
	print_r( bubble(array(5,2,1,9,3,6,8,7,4,10,20,13,17,11,12,18,14,16,19,15)));
	
?>