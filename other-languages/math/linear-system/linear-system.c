/*
Algoritmo para Escalonar Sistemas Lineares
Autor:
    ?
Colaborador:
    ?
Tipo:
    math
Descrição:
    Esta função recebe uma matriz m, n por n, e uma
    matriz R n por 1.
    Ela escalona o sistema mX = R, e atribui a R as
    soluções do sistema.
    Retorna 1, caso tenha sucesso no escalonamento,
    ou 0 caso contrário.
Complexidade:
    O(n^2), sendo n a dimensão do sistema.
Dificuldade:
    medio
*/

int escalonaSistemaLinear(double **m, int n, double R[]){
    int i, j, k;
    for(i=0;i<n;i++){
        if(m[i][i]==0){
            for(j=i+1;j<=n;j++)
                if(j==n)
                    return 0;
                else if(m[j][i]!=0){
                    for(k=0;k<n;k++)
                        m[i][k]+=m[j][k];
                    break;
                }
        }
        R[i]/=m[i][i];
        for(j=0;j<n;j++){
            if(i==j)
                continue;
            R[j]-=R[i]*m[j][i];
        }
        for(k=n-1;k>=i;k--){
            m[i][k]/=m[i][i];
            for(j=0;j<n;j++){
                if(i==j)
                    continue;
                m[j][k]-=m[i][k]*m[j][i];
            }
        }
    }
    return 1;
}

