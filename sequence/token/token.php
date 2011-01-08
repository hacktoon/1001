<?php

/*
Token
Autor: Sérgio Mandrake <sergio_mandrake@yahoo.com.br>
Tipo: sequence
Descrição: Gera um token aleatório
Complexidade:
    Pior caso: ?
    Melhor caso: ?
Dificuldade: fácil
*/

function token($comprimento = 6) {
    $caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    $totalCarac = strlen($caracteres) -1;
    $resultado = '';
    for ($i = 0; $i < $comprimento; $i++) {
        $resultado .= $caracteres[mt_rand(0, $totalCarac)];
    }

    return $resultado;
}

echo token(5);
