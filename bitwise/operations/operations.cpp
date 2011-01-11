/*
Operações bitwise
Autor:
    ?
Colaborador:
    Ramon Caldeira (ramoncaldeira_328@hotmail.com)
Tipo:
    bitwise
Descrição:
    Coletânea de algotitmos bitwise.
Complexidade:  
    O(1)
Dificuldade:
    fácil
*/

/* verifica se um número é par */
bool isOdd(int num) { return num & 1; }

/* verifica se um número é potência de 2
  ex: 16 = 10000(2)
      15 = 01111(2)
      => 16 & 15 = 10000 & 01111 = 0
 */
bool isPower2(int num) { return !(num-1 & num); }

/* permuta case de caractere 
   funcionamento: na tabela ASCII
   os caracteres minúsculos se diferenciam dos maiúsculos
   através do 5° bit = 32 = 20(H)
   ex: A(65) a(97) a - A = 32
*/
void toggleCase(char& ch) { ch ^= 0x20; }

/* seta case maiúsculo */
void toUpper(char& ch) { ch &= ~0x20; }

/* seta case minúsculo */
void toLower(char& ch) { ch |= 0x20; }
