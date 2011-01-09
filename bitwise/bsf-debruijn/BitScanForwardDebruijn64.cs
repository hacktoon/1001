//BitScanForward com De Bruijn (64 bits)
//Autor:
//     Nicolaas Govert de Bruijn
//Tipo:
//    bitwise
//Descrição:
//    Encontra o índice do LSB (Least Significant Bit) em O(1)
//Complexidade:  
//    O(1)
//Dificuldade:
//    facil
//Referências:
//    http://en.wikipedia.org/wiki/De_Bruijn_sequence

using System;

namespace BitScanForwardDebruijn64
{
    class Program
    {
        static int[] index64 = new[] 
        {
           63,  0, 58,  1, 59, 47, 53,  2,
           60, 39, 48, 27, 54, 33, 42,  3,
           61, 51, 37, 40, 49, 18, 28, 20,
           55, 30, 34, 11, 43, 14, 22,  4,
           62, 57, 46, 52, 38, 26, 32, 41,
           50, 36, 17, 19, 29, 10, 13, 21,
           56, 45, 25, 31, 35, 16,  9, 12,
           44, 24, 15,  8, 23,  7,  6,  5
        };

        public static int BitScanForward(ulong value)
        {
            if (value == 0) return -1;
            const ulong debruijn64 = 0x07EDD5E59A4E28C2ul;
            return index64[((value & (~value + 1)) * debruijn64) >> 58];
        }

        static void Main(string[] args)
        {
            Console.WriteLine(BitScanForward(128));
        }
    }
}
