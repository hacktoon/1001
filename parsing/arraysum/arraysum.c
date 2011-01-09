/*
Array Sum
Autor:
    ?
Colaborador:
    Leonardo da Mata barroca at gmail.com
Descricao:
    Esse programa recebe como parametro um nome 
    de um arquivo na entrada, abre esse arquivo 
    para leitura, le os números presentes no 
    arquivo (um numero por linha) e realiza a
    soma desses números.
Complexidade:
    ?
Dificuldade:
    facil
Licenca:
    GPL
 */

#include <stdio.h>
#include <stdlib.h>
int main(int argc, char * argv[]){
    if (argc != 2){
        printf("Usage: %s <file_name>\n",argv[0]);
        exit(1);
    }
    int array_size = 0;
    int* array;
    int i=0;
    int sum=0;
    int num=0;
    FILE *fp; 
    array = (int*)malloc(sizeof(int)*1024);
    fp=fopen(argv[1],"r");
    if(fp==NULL){
        printf("Error opening file\n");
        exit(1);
    }
    while(fscanf(fp, "%d", &num) != EOF){
        array[i]=num;
        i++;
    }
    array_size=i;
    for(i=0;i<array_size;i++){
        sum+=array[i];
    }
    printf("Result: %d\n",sum);
    return 0;
}
