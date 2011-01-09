//Hamming Weight (64 bits)
//Autor:
//    Juan Lopes <juanplopes@gmail.com>
//Tipo:
//    bitwise
//Descrição:
//    Conta o número de bits ligados
//    em um inteiro de 64 bits.
//Complexidade:  
//    Pior caso: O(1)
//    Melhor caso: O(1)
//Dificuldade:
//    facil
//Referências:
//    http://en.wikipedia.org/wiki/Hamming_weight

using System;

namespace HammingWeight64
{
    class Program
    {
        public static int PopCount(ulong x)
        {
            unchecked
            {
                const ulong h01 = 0x0101010101010101;
                const ulong m1 = 0x5555555555555555;
                const ulong m2 = 0x3333333333333333;
                const ulong m4 = 0x0f0f0f0f0f0f0f0f;

                x -= (x >> 1) & m1;
                x = (x & m2) + ((x >> 2) & m2);
                x = (x + (x >> 4)) & m4;
                return (int)((x * h01) >> 56);
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine(PopCount(128));
        }
    }
}
