/*
Mergesort
Autor:
	John von Neumann, em 1945
Colaborador:
	Luiz Fernando Oliveira Corte Real (luiz@vidageek.net)
Tipo:
	sorting
Descrição:
	O algoritmo ordena um vetor dividindo-o pela metade e, depois de processar
	cada metade recursivamente, intercala as metades ordenadas.
Complexidade:
	O(n lgn)
Dificuldade:
	fácil
Referências:
	[1] http://en.wikipedia.org/wiki/Merge_sort
*/

#include <stdio.h>
#define TAMANHO_MAXIMO 100000

/* Intercala duas metades ordenadas do vetor v: de inicio até meio-1 e de meio até fim-1 */
void intercala(int v[], int inicio, int meio, int fim) {
	int vetor_auxiliar[TAMANHO_MAXIMO];
	int indice_parte_1, indice_parte_2, indice_vetor_auxiliar;
	indice_parte_1 = inicio;
	indice_parte_2 = meio;
	indice_vetor_auxiliar = 0;
	/* Mescla as metades até uma delas acabar */
	while (indice_parte_1 < meio && indice_parte_2 < fim) {
		if (v[indice_parte_1] < v[indice_parte_2]) {
			vetor_auxiliar[indice_vetor_auxiliar] = v[indice_parte_1];
			indice_parte_1++;
		} else {
			vetor_auxiliar[indice_vetor_auxiliar] = v[indice_parte_2];
			indice_parte_2++;
		}
		indice_vetor_auxiliar++;
	}
	/* Uma das metades pode ter ficado com elementos sobrando; apenas copiamos esses elementos */
	while (indice_parte_1 < meio) {
		vetor_auxiliar[indice_vetor_auxiliar] = v[indice_parte_1];
		indice_parte_1++;
		indice_vetor_auxiliar++;
	}
	while (indice_parte_2 < meio) {
		vetor_auxiliar[indice_vetor_auxiliar] = v[indice_parte_2];
		indice_parte_2++;
		indice_vetor_auxiliar++;
	}
	/* Copia o vetor auxiliar no lugar certo em v (de trás pra frente para não
	 * ter que calcular o tamanho do pedaço que vamos copiar; esse tamanho já
	 * está na variável indice_vetor_auxiliar) */
	while (indice_vetor_auxiliar > 0) {
		indice_vetor_auxiliar--;
		v[inicio + indice_vetor_auxiliar] = vetor_auxiliar[indice_vetor_auxiliar];
	}
}

/* Ordena o vetor v de inicio até fim-1 */
void mergesort_recursivo(int v[], int inicio, int fim) {
	int meio = (inicio + fim) / 2;
	/* Só chama a recursão na primeira metade se houver mais de um elemento lá */
	if (inicio < meio - 1) {
		mergesort_recursivo(v, inicio, meio);
	}
	/* Idem para a segunda metade */
	if (meio < fim - 1) {
		mergesort_recursivo(v, meio, fim);
	}
	intercala(v, inicio, meio, fim);
}

void mergesort(int v[], int n) {
	mergesort_recursivo(v, 0, n);
}

int main() {
	int vetor[] = { 5, 14, 8, 17, 1, -3, 9};
	int n = 7; /* número de elementos no vetor */
	int i;
	mergesort(vetor, n);
	printf("vetor ordenado:");
	for (i = 0; i < n; i++) {
		printf(" %d", vetor[i]);
	}
	printf("\n");
	return 0;
}
