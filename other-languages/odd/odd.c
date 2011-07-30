/*
Encontrando números Ímpares
Autor:
    ???
Colaborador:
    Filipe Saraiva (filip.saraiva@gmail.com)
Tipo:
    math
Descrição:
    Dá-se um número inteiro não negativo; o algoritmo
    listará todos os números ímpares entre 0 e este número
    dado.
Complexidade:
    O(n)
Dificuldade:
    fácil
*/

#include <stdio.h>

// Função para imprimir os números ímpares
// entre '0' e um número máximo dado.
void numerosImpares(int num){
  
  int contador = 0;
  
  /*
   * Maneira convencional: caso o número a ser comparado
   * tiver o resto da divisão diferente de '0', quer dizer que
   * o número não é um múltiplo de 2 - definição de número ímpar.
   */
  for(contador = 0; contador <= num; contador++){
    
    if((contador % 2) != 0){
      printf("%d ", contador);
    }
  }
  
  /*
   * Maneira esperta - sabemos que o primeiro número ímpar é igual à 1.
   * Daí, basta apenas incrementar o contador em mais duas unidades.
   * Todos os demais números serão ímpares.
   * 
   * Descomente a rotina abaixo para a "Maneira esperta".
   */
//   for(contador = 1; contador <= num; contador = contador + 2){
//     printf("%d ", contador);
//   }
  
  printf("\n");
}

// Função main
int main(){
  
  // Número máximo a ser utilizado.
  // Troque-o por outro número qualquer.
  int limite = 13;
  
  // Chamada da função numerosImpares
  numerosImpares(limite);
  
  return 0;
}
