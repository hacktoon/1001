/*
Algoritimo de troca de variáveis
Autor:
    ?
Colaborador:
    José Ivan Bezerra Vilarouca Filho (ivanfilho2204@hotmail.com)
Tipo:
    bitwise
Descrição:
    Algoritimo que tem objetivo de trocar os valores
	de duas variáveis sem o uso de uma variável temporária
	usando apenas o operdador boolean "ou exclusivo".
	Lembrando que esse algorítimo só funciona se as variáveis
	tiverem em locais diferentes na memória
Complexidade:
    O(1)
Dificuldade:
    fácil
Referências:
	http://en.wikipedia.org/wiki/XOR_swap_algorithm
*/

using System;

public sealed class SwapXor {

	public static void swap(ref int a, ref int b) {
	
		a = a ^ b;
		b = a ^ b;
		a = a ^ b;
	}
	
	public static void Main() {
	
		int var1 = 1234;
		int var2 = 5678;
		
		Console.WriteLine("Valores antes da troca: var1 = {0} var2 = {1}", var1, var2);
		SwapXor.swap(ref var1, ref var2);
		Console.WriteLine("Valores depois da troca: var1 = {0} var2 = {1}", var1, var2);
	}
}