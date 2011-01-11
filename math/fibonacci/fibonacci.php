<?php
/**
 * Sequência de Fibonacci
 *
 * Autor:
 *   ?
 * Colaborador:
 *   Felipe Djinn <felipe@felipedjinn.com.br>
 * Tipo:
 *   math
 * Descrição:
 *   Na matemática, os Números de Fibonacci são uma sequência definida como recursiva.
 *   O algoritmo recursivo que define a série aplica-se, na prática, conforme a regra sugere: 
 *   começa-se a série com 0 e 1; a seguir, obtém-se o próximo número de Fibonacci somando-se 
 *   os dois anteriores e, assim, sucessiva e infinitamente.
 * Complexidade:
 *   F(n) = {
 *      0 se n = 0;
 *      1 se n = 1;
 *      F(n - 1) + F(n - 2)
 *   }
 * Referências:
 *   http://pt.wikipedia.org/wiki/N%C3%BAmero_de_Fibonacci
 */
function fibonacci($n) {
    if ( $n < 2 ) return $n;

    return fibonacci($n - 1) + fibonacci($n - 2);
}

// example
for ( $i = 0; $i <= 20; $i++ ) {
    echo fibonacci($i), '  ';
}

echo "\n";
