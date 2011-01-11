/*
Heap Sort
Autor:
    Robert W. Floyd e J.W.J. Williams.
Colaborador:
    Ramon Caldeira Faria (ramoncaldeira_328@hotmail.com)
Tipo:
    sorting
Descrição:
    O algoritmo serve para ordenar uma estrutura de dados,
    no caso desta implementação um vetor. 
Complexidade:  
    O(n lgn)
Dificuldade:
    medio
*/

void buildMaxHeap(int*, int);
void maxHeapify(int*, int, int);
void swap (int*, int, int);

/***
    - transforma o array numa heap de máximo
    heap: árvore binária com propriedade de heap
    propriedade de heap: um nó deve ser maior que seus filhos.
    
    o array como arvore binaria:
    
    | raiz | n1 | n1 | n2 | n2 | n2 | n2 | ...
    
    - para todos os filhos:
        - retira o nó raiz (maior número) e separa
        - reconstrói a heap
***/
void heapSort(int* array, int size) {  
   buildMaxHeap(array, size);
  
   int n = size;
 
   for (int i=(size-1); i>0; i--) { 
      swap(array, i , 0);
      maxHeapify(array, 0, --n);
   }
}

/* percorre todos os nós que não são folha
e reconstroe-se uma sub-heap tendo ele como raiz
de baixo pra cima */
void buildMaxHeap(int* array, int size) { 
   for (int i = size/2 - 1; i >= 0; i--)
      maxHeapify(array, i , size);
}

/* 
  aplica a propriedade de heap
*/
void maxHeapify(int* array, int pos, int n) { 
   int max = 2 * pos + 1, right = max + 1;
   
   if (max < n) { 
      if ( right < n && array[max] < array[right])
         max = right;
      
      if (array[max] > array[pos]) { 
        swap(array, max, pos);
        maxHeapify(array, max, n);
     }
  }
}

void swap ( int* v, int i, int j ) {
  int aux = v [i];
  v [i] = v [j];
  v [j] = aux;
}
