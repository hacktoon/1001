<?php
	
/*
Bubblesort
Autor: 
	?
Colaborador:
	Maurício Sipmann (sipmann@gmail.com)
Tipo: 
	sorting
Descrição: 
	Varre o vetor comparando cada um dos pares de números
	possíveis e trocando suas posições no vetor se necessário
Complexidade:
	Pior caso: O(n²)
	Melhor caso: O(n²)
Dificuldade:
	facil
Referências:
	http://en.wikipedia.org/wiki/Bubble_sort
*/

	function bubble($valores) {
		$ordenado = false;
		
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
