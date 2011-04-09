/*
Par ou impar
Autor:
    ?
Colaboradores:
    Geraldo Neto email (glnetinho@hotmail.com)
    Prdro Arthur Duarte (pedroarthur.jedi@gmail.com)
Tipo:
    number-theory
Descricao:
   Verifica se os números são impares ou pares.
Complexidade:
    O(n), Através de operação módulo
    O(1), Através de operador binário
Dificuldade:
    facil
*/

#include <stdio.h>

/*
  Macro: retorna 1 se o número for impar ou 0 caso contrário
*/
#define oddOrEven(a) ((a) & 1)

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
