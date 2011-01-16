/*
Par ou impar
Autor:
    ?
Colaborador:
    Geraldo Neto email:glnetinho@hotmail.com
Tipo:
    number-theory
Descricao:
   Verifica se os números são impares ou pares.
Complexidade:
    ?
Dificuldade:
    facil
*/

#include <stdio.h>

void main(void)
{
    int v[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int i, par = 0, impar = 0;
    
    for (i=0; i<=8; i++){ 
        if(v[i]%2==0){
            par=par+1;
        } else {
            impar=impar+1;
        }
    }
    printf("%d numeros pares e %d impares\n", par, impar);
}
