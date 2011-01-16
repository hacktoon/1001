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
using System;
using System.Collections.Generic;

public struct Point {

	public int x;
	public int y;
	
	public Point(int x, int y) {
	
		this.x = x;
		this.y = y;
	}
}

public static class DDA {

	public static Point[] rasteriza(Point ini, Point fim) {
	
		LinkedList<Point> points = new LinkedList<Point>(); //Guardara os pontos criados
		float len;
	
		if (Math.Abs(fim.x - ini.x) >= Math.Abs(fim.y - ini.y)) {
			
			len = Math.Abs(fim.x - ini.x);
		} else {
			
			len = Math.Abs(fim.y - ini.y);
		}
		
		float deltax = (fim.x - ini.x) / len;
		float deltay = (fim.y - ini.y) / len;
		float x = ini.x;
		float y = ini.y;
		
		for (int i = 0; i < len; i++) {
		
			points.AddLast(new Point((int) Math.Floor(x), (int) Math.Floor(y)));
			x += deltax;
			y += deltay;
		}
		
		points.AddLast(new Point((int) Math.Floor(x), (int) Math.Floor(y)));
		
		Point[] ret = new Point[points.Count];
		points.CopyTo(ret, 0);
		
		return ret;
	}
}

public class MainDDA {

	public static void Main() {
	
		Point[] points = DDA.rasteriza(new Point(-2, 3), new Point(10, 15));
		foreach (Point point in points) {
		
			Console.WriteLine("({0}, {1})", point.x, point.y);
		}
	}
}