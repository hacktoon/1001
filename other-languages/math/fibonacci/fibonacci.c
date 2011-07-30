/*
	Fibonacci recursivo e iterativo
Autor:
    Fibonacci
Colaborador:
    José Ivan Bezerra Vilarouca Filho (ivanfilho2204@hotmail.com)
Tipo:
    math
Descrição:
    Algoritmo usado para gerar a sequência de Fibonacci.
	Um termo é a soma de seus 2 antecessores. Sendo os primeiros
	dois termos com valores 0 e 1 respectivamente.
	0, 1, 2, 3, 5, 8, 13, ...
Complexidade:  
    O(n)
Dificuldade:
    facil
*/

#include <stdio.h>

unsigned int fibonacci_recursivo(unsigned int nTermo) {

	if (nTermo == 1) {
	
		return 0;
	} else if (nTermo == 2) {
	
		return 1;
	}
	
	return fibonacci_recursivo(nTermo - 1) + fibonacci_recursivo(nTermo - 2);
}

unsigned int fibonacci_iterativo(unsigned int nTermo) {

	unsigned int ante1 = 0; //Antecessor mais longe
	unsigned int ante2 = 1; //Antecessor mais perto
	int i; //Variável de controle
	
	if (nTermo == 1) {
	
		return 0;
	} else if (nTermo == 2) {
	
		return 1;
	}
	
	for (i = 3; i <= nTermo; i++) {
	
		unsigned int tmp = ante2;
		ante2 = ante1 + ante2;
		ante1 = tmp;
	}
	
	return ante2;
}

//Número de termos que serão gerados pelas funções
#define NTERMOS 22


int main(int argc, char* argv[]) {

	int i;
	
	for (i = 1; i <= NTERMOS; i++) {
	
		printf("%d ", fibonacci_recursivo(i));
	}
	
	putchar('\n');
	
	for (i = 1; i <= NTERMOS; i++) {
	
		printf("%d ", fibonacci_iterativo(i));
	}
	
	return 0;
}