/*
Conversor Decimal/Hexadecimal
Autor:
    ?
Colaborador:
    Ramon Caldeira Faria (ramoncaldeira_328@hotmail.com)
Tipo:
    bitwise
Descrição:
    O algoritmo devolve uma string da representação
    hexadecimal de um determinado inteiro de 8 bits.
Complexidade:
    O(1)
Dificuldade:
    medio
*/

#include <stdlib.h>

const char* HEXA = "0123456789ABCDEF";

/* @param dec número no intervalo [0,255] */
char* decToHex(unsigned dec) {
   char* hexadecimal = (char*) calloc(3, sizeof(char));
   hexadecimal[0] = HEXA[ (dec & 0xF0) >> 4 ];
   hexadecimal[1] = HEXA[ dec & 0x0F ];
   hexadecimal[2] = '\0';
   return hexadecimal;   
}
