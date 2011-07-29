<?php
/*
InsertionSort
Autor:
    ?
Colaborador:    
    Maurício Sipmann ( sipmann@gmail.com )
Tipo:
    sorting
Descrição:
    Varre o vetor organizando-o em ordem crescente.
    Só pula para o próximo elemento depois de organizar todos os elementos anteriores.
Complexidade:
    O(n²)
Dificuldade:
    facil
Referências:
    http://pt.wikipedia.org/wiki/Insertion_sort
*/

/*
 * Parâmetros
 * vetor
 *      Vetor de números inteiros
 */
function insertionSort($vetor)
{
    //Vamos começar o loop pelo segundo elemento do vetor
    for($i=1;$i<count($vetor);$i++)
    {

        $anterior = $i-1;

        $proximo = $anterior + 1;

        $troca = true;

        while($troca)
        {
            if($vetor[$anterior] > $vetor[$proximo])
            {
                $tmp = $vetor[$anterior];
                $vetor[$anterior] = $vetor[$proximo];
                $vetor[$proximo] = $tmp;
            }
            else
                $troca = false;

            $anterior--;
            $proximo = $anterior + 1;

            if ($anterior<0)
                $troca = false;
        }
    }
	
	return $vetor;
	
}


$vetor = array(98, 78, 2, 4, 100, -2 );
$vetor = insertionSort($vetor);

for($i=0; $i<count($vetor); $i++)
	echo $vetor[$i].'<br>';

?>