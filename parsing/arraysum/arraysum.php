<?php
/*
Array Sum
Autor:
    ?
Colaborador:
    Mauricio sipmann ( sipmann@gmail.com )
Descricao:
    Essa funчуo recebe um nome de arquivo po parametro,
    le esse arquivo e retorna a soma dos seus valores internos.
Complexidade:
    ?
Dificuldade:
    facil
Licenca:
    GPL
 */

    function SomaArq($arquivo) {
		$arq = file($arquivo);
		
		foreach($arq as $num) {
			$soma += $num;
		}
		
		return $soma;
	}
	$resultado = SomaArq('somas.txt');
	echo $resultado;
  
?>