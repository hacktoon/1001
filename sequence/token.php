<?php

/*
Token
Autor: Sérgio Mandrake <sergio_mandrake@yahoo.com.br>
Tipo: ?
Descrição: Gera um token aleatório
Complexidade:
    Pior caso: ?
    Melhor caso: ?
*/

function token($comprimento = 6) {
    $caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    $totalCarac = strlen($caracteres) -1;
    $resultado = '';
    for ($i = 0; $i < $comprimento; $i++) {
        $resultado .= $caracteres[mt_rand($i, $totalCarac)];
    }

    return $resultado;
}

echo token(5);
