/*
Exponenciação
Autor:
	?
Colaborador:
	Dayvid Victor (victor.dvro@gmail.com)
Tipo:
	math
Descrição:
	Calcula a exponenciação, X elevado a N,
	sendo X qualquer valor e N um valor inteiro.
	Sendo feito desta forma, a complexidade se
	resume a O(log n), enquanto que a implementação
	iterativa ficaria O(n).
Complexidade:  
	O(log n)
Dificuldade:
	facil
Referências: (opcional)
	?
*/
#include <stdio.h>
#include <stdlib.h>

float recursive_pow (float x, int n)
{
	if (n == 1)
		return x;

	if (n == 0)
		return 1;
	
	if (n < 0 && x != 0)
		return 1 / recursive_pow(x, -n);

	if (x == 0)
		return 0;

	float pow = recursive_pow (x, n/2);
	pow = pow * pow * recursive_pow(x, n % 2);
	return pow;
}

int main(void)
{
	float x[] = {-3, -2, -1, 0, 1, 2, 3};
	int n[] = {-3, -2, -1, 0, 1, 2, 3};
	int i;
	int j;
	for (i = 0; i < 7; i++)
		for (j = 0; j < 7; j++)
			printf("%f^%d=%f\n",x[i], n[j], recursive_pow(x[i],n[j]));
	
	return 0;
}
