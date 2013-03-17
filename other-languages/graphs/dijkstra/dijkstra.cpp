/*
Algoritmo de Dijkstra (com matriz de adjacências)
Autores: 
    Edsger Dijkstra
Colaborador:
    Luiz Rodrigo (luizrodri.go@hotmail.com)
Alteração:
	Péricles Lopes Machado (pericles.raskolnikoff@gmail.com)
Tipo: 
    graphs
Descrição: 
    O Algoritmo de Dijsktra é um algoritmo em grafos clássico que determina a
    menor distância de um determinado vértice para todos os outros. Essa é a
    implementação utilizando matriz de adjacências, que tem desempenho 
    inferior.
Complexidade: 
    O(|E| log |V|)
Dificuldade: 
    medio
Referências:
    [1] http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    [2] Cormem, Thomas H. Introduction to Algorithms, 3rd Edition. 
        ISBN 978-0-262-53305-8. Páginas 658-659.
*/

#include <iostream>
#include <queue>
#include <vector>
#include <stdio.h>

using namespace std;

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

    // define a lista de adjascencias que é uma representação melhor 
	// para o algoritmo de Dijkstra. Lembrando que representação é 
	// uma parte importante na construção de um algoritmo eficiente

	typedef vector<vector<int> > Graph;
	Graph G(n);

    // inicializa (todas as menores distâncias como infinito)
    for (int i = 0; i < n; i++) { 
        min_dist[i] = INFINITY;
        previous[i] = -1;

		// cria a lista de adjascências
		for (int j = 0; j < n; ++j)
			if (i != j and dist[i][j] < INFINITY) {
				G[i].push_back(j);
			}
    }
    
    // exceto a da origem para a origem, que é 0
    min_dist[origin] = 0;
    
	// heap utilizada para acelerar a busca pelo melhor opção atual
	typedef pair<int, int> Pair;
	priority_queue<Pair> Q;
	
	// a distancia atual para a origin é utilizada como primeira chave para a ordenação da heap
	Q.push(Pair(0, origin));

    while (!Q.empty()) {
		int u = Q.top().second; 
		Q.pop();
    
        for (int i = 0; i < G[u].size(); i++) {
			int v = G[u][i];
            if  (min_dist[u] + dist[u][v] < min_dist[i]) {
                min_dist[v] = min_dist[u] + dist[u][v];
                previous[v] = u;

				// como a priority_queue utiliza a chave de mais alta prioridade para ordenar
				// basta multiplar por -1 a estimativa atual para ordenar adequadamente a heap
				Q.push(Pair(-min_dist[v], v));
            }
		}
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

