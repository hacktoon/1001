/*
Método numérico para resolução de raiz enésima
Autor:
    ?
Colaborador:
    Guilherme de Sales Orioli gui.orioli@gmail.com
Tipo:
    math
Descrição:
    Tira a raíz n-ésima de x, permitindo um erro máximo de error-allowed
Exemplo:
    root(-123,5,0.0001);
   
    Saída: -2.618068900925607
   
Complexidade:
    ?
Dificuldade:
    ?
*/

public class MetodosNumericos{

    public static void main(String args[]){
        System.out.println(root(16, 2, 0.000001));
    }
   
   
    public static double root (double x, int n, double error_allowed){
        double r,test=0;
        int i;
        boolean negative = false;
        boolean fraction = false;
       
        if (x < 0){
            if(n%2==0)
                return 0;
            negative = true;
            x = -x;
        }
       
        if ( (x>0) && (x<1)){
            x = 1/x;
            fraction = true;
        }
       
        r=x;
        test=x+1;
        while ( (test < x-error_allowed) || (test > x+error_allowed) ){
            if (test<x)
                r=r+r/2;
            else
                r=r-r/2;
           
            test=r;
           
            for (i=0; i<(n-1); i++)
                test*=r;
        }
       
        if(fraction){
            r = 1/r;
        }
       
        if(negative){
            r = -r;
        }
       
        return r;
    }
}
