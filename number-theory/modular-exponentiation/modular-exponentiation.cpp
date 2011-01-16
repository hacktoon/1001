/*
Exponenciação modular (utilizando representação binária)
Autor: 
    ?
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo:
    number-theory
Descrição: 
    É um algoritmo que realiza eficientemente a exponenciação modular, ou seja,
    calculos do tipo a^b mod n. Esse tipo de cálculo é de extrema importância
    para a teoria dos números e para a criptografia, é uma das operações mais
    importantes no método de criptografia RSA.
Complexidade:
    O(log b)
Dificuldade: 
    medio
Referências:
    http://en.wikipedia.org/wiki/Modular_exponentiation
    Cormem, Thomas H. Introduction to Algorithms, 3rd Edition. 
        ISBN 978-0-262-53305-8. Página 957.
*/

#include <iostream>

int modular_exponentiation(int a, int b, int n) {
    int result, aux = 1;
    
    // aux: auxiliar para fazer a conversão binária de b
    // inicia com a potência de base 2 mais próxima de b
    while ( aux < b ) 
        aux <<= 1;
    
    result = 1;
    
    // enquanto aux > 0
    while ( aux ) {
        result = (result*result) % n;
        
        // se o dígito de b for 1
        if ( b & aux )
            result = (a*result) % n; 
        
        // divide por 2
        aux >>= 1;
    }
    
    return result;
}

int main( ) {
    
    std::cout << modular_exponentiation(5, 10, 30) << "\n";
    std::cout << modular_exponentiation(3, 11, 5) << "\n";
    std::cout << modular_exponentiation(11, 7, 17) << "\n";
    
    return 0;
}
