<?php
/*
Quicksort
Autor:
    Bruno Ricardo Siqueira
Tipo:
    sorting
Descrição:
    Quicksort é um algorítmo de ordenação de vetores cuja estratégia é
    dividir para conquistar. Basicamente o algorítmo organiza os elementos
    dos vetores de forma que os menores estejam antes dos maiores.
    Esse passo é feito recursivamente até que a lista completa esteja ordenada.
Complexidade:  
    O(n log(n)) - Melhor caso e médio caso.
    O(n²) - Pior caso.
Dificuldade:
    facil
Referências:
    http://pt.wikipedia.org/wiki/Quicksort#C
*/

function quicksort($vetor) {
	if (count($vetor) <= 1) {
		return $vetor;
	}
 
	$chave = array_shift($vetor);

	return	array_merge(
				quicksort(array_filter($vetor, function ($valor) use($chave) {
					return $valor < $chave;
				})),
			array($chave),
				quicksort($higher = array_filter($vetor, function ($valor) use($chave) {
					return $valor >= $chave;
				}))
			);
}

$vet = array(2, 7, 3, 8, 4, 9, 1, 0, -1);

$tam = count($vet);

for ($i = 0; $i < $tam; $i++){
	echo $vet[$i];
}

echo "\n";

$vet_ordenado = quicksort($vet);

for ($i = 0; $i < $tam; $i++){
	echo $vet_ordenado[$i];
}
echo "\n";
?>