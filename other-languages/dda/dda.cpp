/*
DDA (Digital Differential Analyzer)
Autor:
    ?
Colaborador:
    José Ivan Bezerra Vilarouca Filho (ivanfilho2204@hotmail.com)
Tipo:
	math
Descrição:
    DDA é um algoritmo de interpolação linear entre dois pontos, inicial e final.
	Ele é muito usado na área de Computação Gráfica para rasterizar linhas e polígonos.
Complexidade:  
    O(n)
Dificuldade:
    facil
Referências:
    http://www.dca.fee.unicamp.br/courses/IA725/1s2006/notes/n4.pdf
	http://en.wikipedia.org/wiki/Digital_Differential_Analyzer_(graphics_algorithm)
*/

#include <list>
#include <iostream>
#include <cstdlib>
#include <cmath>

typedef struct Point {

	public:
	
		int x;
		int y;
		
		Point(int x, int y) {
			
			this->x = x;
			this->y = y;
		}
	
} Point;

class DDA {

	public:
		
		static std::list<Point>& rasteriza(const Point ini, const Point fim) {
		
			std::list<Point>* points = new std::list<Point>(); //Guardara os pontos criados
			float len;
		
			if (abs(fim.x - ini.x) >= abs(fim.y - ini.y)) {
				
				len = abs(fim.x - ini.x);
			} else {
				
				len = abs(fim.y - ini.y);
			}
			
			float deltax = (fim.x - ini.x) / len;
			float deltay = (fim.y - ini.y) / len;
			float x = ini.x;
			float y = ini.y;
			
			for (int i = 0; i < len; i++) {
			
				points->push_back(Point((int) floor(x), (int) floor(y)));
				x += deltax;
				y += deltay;
			}
			
			points->push_back(Point((int) floor(x), (int) floor(y)));
			
			return *points;
		}
		
	private:
	
		DDA() {}
		~DDA() {}
};

using namespace std;
int main(int argc, char* argv[]) {

	list<Point> points = DDA::rasteriza(Point(-2, 3), Point(10, 15));
	list<Point>::iterator it;
	
	for (it = points.begin(); it != points.end(); it++) {
	
		cout << "(" << it->x << ", " << it->y << ")" << endl;
	}
	
	return 0;
}
