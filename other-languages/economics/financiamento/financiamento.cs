/*
Financiamento
Autor:
    ?
Colaborador:
    Bruno Lara Tavares <bruno.exz@gmail.com>
Tipo:
    ?
Descrição:
	Calcula o valor das parcelas do financiamneto
	baseado no capital inicial e taxa de juros
	de acordo na função Price
Complexidade:
    ?
Dificuldade:
    facil
Referências:
    http://pt.wikipedia.org/wiki/Tabela_price#C.C3.A1lculo
*/


using System;

namespace financiamneto
{
	class MainClass
	{
		static public double financiamneto(double investimento, double juros, int periodo)
		{
			return (investimento*juros) / (1 - (1/Math.pow((1+juros),periodo));
		}
		
		public static void Main (string[] args)
		{
			Console.WriteLine (financiamneto(1000,0.03,4));
			Console.ReadKey();
		}
	}
}
