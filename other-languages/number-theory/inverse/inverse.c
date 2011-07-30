/*

Inverse
Autor:
    JoseFernandoTolentino (JoseFernandoTolentino@gmail.com)
Tipo:
    number-theory
Descrição:
    Inverte os algarismos de um número
Complexidade:  
    Pior caso: O(infinito)
    Melhor caso: O(n)
Dificuldade:
    facil
Referências:
*/

#include <stdio.h>

int inverse(int input)
{
  int x=input;
  int output=0;
  while (x>0) {
    output = output * 10 + x % 10;
    x = x / 10;
  }
  return output;
}

int main()
{
    int input = 12345;
    int output= inverse(input);
    printf("Numero=%d\ninverso=%d\n", input, output);
    return 0;
}
 
