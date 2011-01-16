<?php
/*
DDA (Digital Differential Analyzer)
Autor:
    ?
Colaborador:
    José Ivan Bezerra Vilarouca Filho (ivanfilho2204@hotmail.com)
Tipo:
	math
Descrição:
    DDA é um algoritmo de interpolação linear entre dois pontos, inicial e final.
	Ele é muito usado na área de Computação Gráfica para rasterizar linhas e polígonos.
Complexidade:  
    O(n)
Dificuldade:
    facil
Referências:
    http://www.dca.fee.unicamp.br/courses/IA725/1s2006/notes/n4.pdf
	http://en.wikipedia.org/wiki/Digital_Differential_Analyzer_(graphics_algorithm)
*/

class Point {

	public $x;
	public $y;
	
	public function __construct($x, $y) {
	
		$this->x = $x;
		$this->y = $y;
	}
}

class DDA {

	public static function rasteriza($ini, $fim) {
	
		$points = array();
		$len;
	
		if (abs($fim->x - $ini->x) >= abs($fim->y - $ini->y)) {
			
			$len = abs($fim->x - $ini->x);
		} else {
			
			$len = abs($fim->y - $ini->y);
		}
		
		$deltax = ($fim->x - $ini->x) / $len;
		$deltay = ($fim->y - $ini->y) / $len;
		$x = $ini->x;
		$y = $ini->y;
		
		for ($i = 0; $i < $len; $i++) {
		
			$points[] = new Point(floor($x), floor($y));
			$x += $deltax;
			$y += $deltay;
		}
		
		$points[] = new Point(floor($x), floor($y));
		
		return $points;
	}
}

$points = DDA::rasteriza(new Point(-2, 3), new Point(10, 15));
foreach ($points as $point) {

	echo "($point->x, $point->y)<br />";
}
?>