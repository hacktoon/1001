# -*- coding: utf-8 -*-

"""
Algoritmo A* 
Autores: 
    Peter Hart, Nils Nilsson and Bertram Raphael 
Colaborador:
 	Péricles Lopes Machado [gogo40] (pericles.raskolnikoff.gmail.com)
Tipo: 
    graphs
Descrição: 
    O Algoritmo A* é uma generalização do algoritmo de Dijkstra que
permite acelerar a busca com uma heuristica que utiliza propriedades do grafo 
para estimar a distância para o destino. Este algoritmo é ideal quando aplicados
em grades ou representações espaciais e em situações em que já conhecemos a
posição do destino.

Complexidade: 
    O(|E| log |V|)
Dificuldade: 
    medio
Referências:
    [1] http://en.wikipedia.org/wiki/A*_search_algorithm
    [2] http://falapericles.blogspot.com.br/2009/05/o-algoritmo.html
"""

"""
Função para imprimir o caminho
"""
def imprime_caminho(pi, u):
	ux = u[0];
	uy = u[1];

	if pi[ux][uy] == None:
		print u;
	else:
		imprime_caminho(pi, pi[ux][uy]);
		print u;

"""
Função para 'renderizar' o jogador numa posição da grade
"""
def renderizar_grade(G, ux, uy):
	l = list(G[ux]);
	l[uy] = 'x';
	G[ux] = "".join(l);

	for i in range(0, len(G)):
		print " ", G[i];

	print "---------";

	l = list(G[ux]);
	l[uy] = '.';
	G[ux] = "".join(l);

"""
Função para 'renderizar' a trajetória percorrida
"""
def renderizar_caminho(pi, G, u):
	ux = u[0];
	uy = u[1];

	if pi[ux][uy] == None:
		renderizar_grade(G, ux, uy);
	else:
		renderizar_caminho(pi, G, pi[ux][uy]);
		renderizar_grade(G, ux, uy);

from heapq import *;
from math import *;


"""
Este algoritmo utiliza uma grade para realizar a busca.
A origem é marcada com o símbolo 'x' e o destino é marcado
com o simbolo '+'.

"""
G = [
"###..####################..####################..####################..####################..#################.",
".........*........#.#..........*........#.#...........*........#.#...........*........#.............*.......#..",
"....#....#.##.#####.#......#....#.##.#####.#......#....#.##.#####.#......#....#.##.#####........#....#.##.###..",
"#...#....#..#......*..#...#....#..#......*..#...#....#..#......*..#...#....#..#......*......#....#..#......*...",
"#.####...#*##+.....*.##.####...#*##......*.##.####...#*##......*.##.####...#*##......*.##.####...#*##......*.#.",
"#....#..##.........#.##....#..##.........#.##....#..##.........#.##....#..##.........#.##..................#.#.",
"#....#...#.###.##..####....#...#.###.##..####....#...#.###.##..####....#...#.###.##..####........#.###.##..###.",
"#....#.......#..#....##....#.......#..#....##....#.......#..#....##....#...............##............#..#....#.",
"#....#.......#..#....##....#.......#..#....##....#.......#..#....##....#.............................#..#....#.",
"###..#.##########.#######..#.##########.#######..#.##########.#######..#.##########.##.####..#.##########.####.",
"#...##.....#....#.#.......##.....#....#.#..##...##.....#....#.#.......##.....#....#.#.......##.....#....#.#..#.",
"#..........#.....................#.........##..........#.....................#.........##..........#.........#.",
"###..#.....##############..#.....##############..#.x...##############..#.....#########.####..#.....######..###.",
".........*.....................*......................*........#.#...........*..........#...........*.......#..",
"....#....#.##.#####.#......#....#.##.#####.#......#....#.##.#####.#......#....#.##.#####.#......#....#.##..##..",
"#...#....#..#......*..#...#....#..#......*..#...#....#..#......*...........#..#......*..#...#....#..#......*...",
"#.####...#*##......*.##.####...#*##......*.##.####...#*##......*.##.####...#*##......*.##.####...#*##......*.#.",
"#....#..##.........#.##....#..##.........#.##....#..##.........#.##....#..##.........#.......#..##.........#.#.",
"#....#...#.###.##..####....#...#.###.##..####....#...#.###.##..####....#...#.###.##..####....#...#.###.##..###.",
"#....#.......#..#....##....#.......#..#....##....#.......#..#....##....#.......#..#....##............#..#....#.",
"#....#.......#..#....##....#.......#..#....##....#.......#..#....##....#.......#..#....##....#.......#..#....#.",
"###..#.##########.#######..#.##########.#######..#.##########.#######..#.##########.#######..#.##########.####.",
"#...##.....#....#.#..##...##.....#....#.#..##...##.....#....#.#..##...##.....#....#.#..##...##.....#....#.#..#.",
"#..........#.........##..........#.........##..........#.........##..........#.........##..........#.........#.",
"###..#.....##############..#.....##############..#.....##############..#.....##############..#.....###########.",
"..............................................................................................................."];

"""
Localizando a posição do jogador ('x') e do destino ('+')
e inicializa matriz com estimativa de distância D.
"""

D = [];
pi = [];
for x in range(0, len(G)):
	D += [[]];
	pi += [[]];
	for y in range(0, len(G[x])):
		D[x] += [None];
		pi[x] += [None];
		if G[x][y] == 'x':
			s = (x, y);
			l = list(G[x]);
			l[y] = '.';
			G[x] = "".join(l);
		elif G[x][y] == '+':
			t = (x, y);

"""
Possibilidades de movimentação:
...
.x.
...
"""

dx = [-1, -1, -1,  0,  0,  1,  1,  1];
dy = [-1,  0,  1, -1,  1, -1,  0,  1];


"""
Heurística que estima a distancia para o destino:

H(p, t) = sqrt((p.x - t.x)^2 + (p.y - t.y)^2)

Nesse código utilizamos o quadrado da distância euclidiana como estimativa.
"""

def H(s, t):
	Dx = s[0] - t[0];
	Dy = s[1] - t[1];
	return sqrt(Dx * Dx + Dy * Dy);

def dist(s, t):
	Dx = s[0] - t[0];
	Dy = s[1] - t[1];
	return sqrt(Dx * Dx + Dy * Dy);



Q = [];

D[s[0]][s[1]] = 0;
heappush(Q, (0, s));

"""
Enquanto a fila de prioridade não estiver vazia tente verificar se o topo
da fila é melhor opção de rota para se chegar nos adjascentes. Como o topo
já é o mínimo, então garante-se que D[u] já está minimizado no momento.
"""
while Q:
	p = heappop(Q)[1];

	u = (p[0], p[1]);
	ux = u[0];
	uy = u[1];

	"""
	Como já chegamos no destino, podemos parar a busca
	"""
	if u == t:
		break;

	for i in range(0, len(dx)):
		vx = u[0] + dx[i];
		vy = u[1] + dy[i];

		v = (vx, vy);

		duv = dist(u, v);
		if vx > -1 and vx < len(G):
			if vy > -1 and vy < len(G[vx]): 
				if (D[vx][vy] > D[ux][uy] + duv or D[vx][vy] == None) and G[vx][vy] != '#':
					D[vx][vy] = D[ux][uy] + duv;
					pi[vx][vy] = u;
					"""
					A única diferença entre o A* e o dijkstra é o modo como é ordenado a heap.
					No caso, ela utiliza a heurítica H que procura colocar no topo os pontos mais
					próximos do destino.
					"""
					heappush(Q, (D[vx][vy] + H(v, t), v));
		

if D[t[0]][t[1]] != None:
	print "A distância entre s e t é: ", D[t[0]][t[1]]; 
	"""
	Descomente essa linha caso queira ver a sequencia de passos percorrido pelo jogador
	"""
	imprime_caminho(pi, t);
	"""
	Descomente essa linha se quiseres ver o caminho percorrido na grade
	"""
	#renderizar_caminho(pi, G, u);
else:
	print "Não existe caminho entre s e t!"

