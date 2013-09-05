/*
   Soma de Gauus  -  Gauss Sum
Autores: 
	Carl Friedrich Gauss    
Colaborador:
    Kaio Turubia (kaiokot@gmail.com)
Tipo: 
    math
Descrição: 
     É um algoritmo que, dado um número, é a realizada a soma de 1 até o número informado.
	Ex: Soma de 1 a 100:
	S = 1+2+3+...+99+100 = 5050
	Ex: Soma de 1 a 100:
	S = 1+2+3+...+99+100 = 5050
Complexidade: 
    ?
Dificuldade: 
    facil
Referências:
    [1] http://pt.wikipedia.org/wiki/Soma_de_Gauss

*/
#include <iostream>

int gaussSum(int number)
{
    int result;
    result = number * (number + 1) / 2;
    return (result);
}

int main ()
{   
	int number = 100;
	int result;   
	result = gaussSum(number);
	std::cout << "The sum value is : " << result;
	return 0;
}
