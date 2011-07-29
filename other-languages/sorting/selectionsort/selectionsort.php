<?php
/*
Selection Sort
Autor: 
    ?
Colaborador:
    Maurэcio Sipmann (sipmann@gmail.com)
Tipo: 
    sorting
Descriчуo: 
    Щ um algoritmo de ordenaчуo que consiste em pesquisar o menor elemento
    e colocar na primeira posiчуo, o segundo menor e colocar na segunda 
    posiчуo e assim sucessivamente, atщ que a sequъncia esteja ordenada.
    Щ uma excelente escolha quando hс necessidade quando o custo de 
    escrita щ alto, pois ele realiza em torno de 2n operaчѕes de escrita. [2]
Complexidade de tempo: 
    O(nВ)
Dificuldade: 
    facil
Referъncias:
    [1] http://en.wikipedia.org/wiki/Selection_sort
    [2] http://en.wikipedia.org/wiki/Selection_sort#Comparison_to_other_sorting_algorithms
*/

function selection_sort($a) {
    
    for ($i = 0; $i < count($a)-1; $i++) {
        $min = $i;
		
        for ($j = $i + 1; $j < count($a); $j++)
            if ( $a[$j] < $a[$min] )
                $min = $j;
                
        $temp = $a[$i];
        $a[$i] = $a[$min];
        $a[$min] = $temp;
    }
	
	return $a;
}

$a = array(6, -2, 3, 5, 7, 4, 3);
$a = selection_sort($a);
    
for($i = 0; $i < 7; $i++)
	echo $a[$i] ."<br>";

?>