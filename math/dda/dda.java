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

import java.awt.Point;
import java.util.LinkedList;

public class dda {

	public static Point[] rasteriza(Point ini, Point fim) {
	
		LinkedList<Point> points = new LinkedList<Point>(); //Guardara os pontos criados
		float len;
	
		if (Math.abs(fim.x - ini.x) >= Math.abs(fim.y - ini.y)) {
			
			len = Math.abs(fim.x - ini.x);
		} else {
			
			len = Math.abs(fim.y - ini.y);
		}
		
		float deltax = (fim.x - ini.x) / len;
		float deltay = (fim.y - ini.y) / len;
		float x = ini.x;
		float y = ini.y;
		
		for (int i = 0; i < len; i++) {
		
			points.add(new Point((int) Math.floor(x), (int) Math.floor(y)));
			x += deltax;
			y += deltay;
		}
		
		points.add(new Point((int) Math.floor(x), (int) Math.floor(y)));
		
		return points.toArray(new Point[0]);
	}
	
	public static void main(String[] args) {
	
		Point[] points = dda.rasteriza(new Point(-2, 3), new Point(10, 15));
		for (Point point : points) {
		
			System.out.printf("(%d, %d)\n", point.x, point.y);
		}
	}
	
}