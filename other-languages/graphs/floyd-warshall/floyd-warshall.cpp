/*
Algoritmo de Floyd-Warshall
Autores: 
    Robert Floyd e Stephen Warshall
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo: 
    graphs
Descrição: 
    O Algoritmo de Floyd-Warshall, a partir de uma grafo representado
    em uma matriz (matriz de adjacências), determina as menores distâncias
    entre todos os pares (ou seja, as menores distâncias de todos os 
    vértices para todos os vértices).
Complexidade: 
    O(|V|³)
Dificuldade: 
    medio
Referências:
    [1] http://en.wikipedia.org/wiki/Floyd-Warshall
    [2] Cormem, Thomas H. Introduction to Algorithms, 3rd Edition. 
        ISBN 978-0-262-53305-8. Páginas 693-695.
*/

#include <iostream>

/*
Parâmetros:
    dist: a matriz de adjacências contendo as distâncias entre os vértices
*/

const int n = 3;

void floyd_warshall(int dist[n][n]) {
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) 
                if ( dist[i][k] + dist[k][j] < dist[i][j] )
                    dist[i][j] = dist[i][k] + dist[k][j];
}

int main( ) {
    int dist[n][n] = { 
        {0, 3, 10},
        {3, 0, 1000},
        {10, 1000, 0}
    };

    floyd_warshall(dist);
    
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            std::cout << "Menor distancia de " << i << " para " << j << ": " 
                    << dist[i][j] << "\n";
    return 0;
}
