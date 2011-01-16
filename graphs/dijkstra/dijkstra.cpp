/*
Algoritmo de Dijkstra (com matriz de adjacências)
Autores: 
    Edsger Dijkstra
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Tipo: 
    graphs
Descrição: 
    O Algoritmo de Dijsktra é um algoritmo em grafos clássico que determina a
    menor distância de um determinado vértice para todos os outros. Essa é a
    implementação utilizando matriz de adjacências, que tem desempenho 
    inferior.
Complexidade: 
    O(|V|²)
Dificuldade: 
    medio
Referências:
    [1] http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    [2] Cormem, Thomas H. Introduction to Algorithms, 3rd Edition. 
        ISBN 978-0-262-53305-8. Páginas 658-659.
*/

#include <iostream>
#include <stdio.h>

/*
Parâmetros:
    dist: a matriz de adjacências contendo as distâncias entre os vértices
*/

const int n = 5;
const int INFINITY = (1 << 30)-1; // 2^30-1

/*
Parâmetros:
    dist: matriz de adjacências que contém as distâncias entre os vértices
    origin: o vértice a partir do qual serão calculadas as menores distâncias
    min_dist: vetor para armazenar as menores distâncias calculadas com o algoritmo
    previous: vetor para armazenar o vértice anterior para chegar ao vértice atual
        (permite determinar as rotas).
*/
void dijkstra(int dist[n][n], int origin, int min_dist[n], int previous[n]) {
    int i, min, ncomputed = 0;
    bool computed[n];
    
    // inicializa (todas as menores distâncias como infinito)
    for (i = 0; i < n; i++) { 
        min_dist[i] = INFINITY;
        previous[i] = -1;
        computed[i] = false;
    }
    
    // exceto a da origem para a origem, que é 0
    min_dist[origin] = 0;
    
    while ( ncomputed < n ) {
    
        for (min = 0; computed[min]; min++);
        
        for (i = min + 1; i < n; i++)
            if ( computed[i] == false && min_dist[i] < min_dist[min] )
                min = i;        
                
        for (i = 0; i < n; i++)
            if ( min_dist[min] + dist[min][i] < min_dist[i] ) {
                min_dist[i] = min_dist[min] + dist[min][i];
                previous[i] = min;
            }
        
        computed[min] = true;
        ncomputed++;
    }
}

void print_path(int previous[], int n) {
    if ( previous[n] != -1 ) {
        print_path(previous, previous[n]);
        printf("-> %d ", n);
    } else 
        printf("%d ", n);
}

int main( ) {

    // Visualização desse grafo: http://i52.tinypic.com/2qx6z2p.png
    // Distâncias INFINITY indicam que não há aresta que ligue os dois vértices
    int dist[n][n] = {
        {0, 10, INFINITY, 5, INFINITY},
        {INFINITY, 0, 1, 2, INFINITY},
        {INFINITY, INFINITY, 0,  INFINITY, 4},
        {INFINITY, 3, 9, 0, 2},
        {2, INFINITY, 6, INFINITY, 0}};
    int min_dist[n], prev[n];
    
    dijkstra(dist, 0, min_dist, prev);
    
    for (int i = 1; i < n; i++) {
        printf("Shortest path from 0 to %d: ", i); 
        print_path(prev, i);
        printf(". Distance: %d\n", min_dist[i]);
    }
        
    return 0;
}
