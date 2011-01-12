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

public class fibonacci {

	public static int fibonacci_recursivo(int ntermo) {
	
		if (ntermo < 0) {
		
			throw new IllegalArgumentException("Term position must be greater than 0");
		} else if (ntermo == 1) {
		
			return 0;
		} else if (ntermo == 2) {
		
			return 1;
		}
		
		return fibonacci_recursivo(ntermo - 1) + fibonacci_recursivo(ntermo - 2);
	}
	
	public static int fibonacci_iterativo(int ntermo) {
	
		if (ntermo < 0) {
		
			throw new IllegalArgumentException("Term position must be greater than 0");
		} else if (ntermo == 1) {
		
			return 0;
		} else if (ntermo == 2) {
		
			return 1;
		}
		
		int ante1 = 0;
		int ante2 = 1;
		for (int i = 3; i <= ntermo; i++) {
		
			int tmp = ante2;
			ante2 = ante1 + ante2;
			ante1 = tmp;
		}
		
		return ante2;
	}
	
	public static void main(String[] args) {
	
		for (int i = 1; i < 15; i++) {
		
			System.out.print(fibonacci.fibonacci_recursivo(i) + " ");
		}
		
		System.out.println();
		
		for (int i = 1; i < 15; i++) {
		
			System.out.print(fibonacci.fibonacci_iterativo(i) + " ");
		}
	}
}