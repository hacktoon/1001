/*
Cálculo de fatorial
Autor:
    ?
Colaborador:
    Bruno Lara Tavares <bruno.exz@gmail.com>
Tipo:
    math
Descrição:
    Calcula o fatorial de um número
Complexidade:  
    ?
Dificuldade:
    facil
*/


using System;

namespace fatorial
{
	class MainClass
	{
		static public double fatorial(int num)
		{
			return num > 1 ?num*fatorial(num-1):1;
		}
		
		public static void Main (string[] args)
		{
			Console.Write ("Digite o numero para calcular o fatorial: ");
			Console.WriteLine (fatorial(int.Parse(Console.ReadLine())));
			Console.ReadKey();
		}
	}
}
