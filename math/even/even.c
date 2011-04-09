/*
Encontrando números Pares
Autor:
    ???
Colaboradores:
    Filipe Saraiva (filip.saraiva@gmail.com)
    Pedro Arthur Duarte (pedroarthur.jedi@gmail.com)
Tipo:
    math
Descrição:
    Dá-se um número inteiro não negativo; o algoritmo
    listará todos os números pares entre 0 e este número
    dado.
Complexidade:
    O(n)
Dificuldade:
    fácil
*/

#include <stdio.h>

// Função para imprimir os números pares
// entre '0' e um número máximo dado.
void numerosPares(int num){
  
  int contador = 0;
  
  /*
   * Maneira convencional: caso o número a ser comparado
   * tiver o resto da divisão igual a '0', quer dizer quer
   * o número é um múltiplo de 2 - definição de número par.
   */
  for(contador = 0; contador <= num; contador++){
    
    if((contador % 2) == 0){
      printf("%d ", contador);
    }
  }
  
  /*
   * Maneira esperta - sabemos que o primeiro número par é igual à 0.
   * Daí, basta apenas incrementar o contador em mais duas unidades.
   * Todos os demais números serão pares.
   * 
   * Descomente a rotina abaixo para a "Maneira esperta".
   */
//   for(contador = 0; contador <= num; contador = contador + 2){
//     printf("%d ", contador);
//   }
  
  printf("\n");
}

/* Via aritimética binária (maneira convencional) */
void numerosPares_2(int num) {
  int contador;
  
  for (contador = 0 ; contador <= num ; contador++)
    if ((contador & 1) == 0)
      printf("%d ", contador);
}

// Função main
int main(){
  
  // Número máximo a ser utilizado.
  // Troque-o por outro número qualquer.
  int limite = 13;
  
  // Chamada da função numerosPares
  numerosPares(limite);
  
  return 0;
}
