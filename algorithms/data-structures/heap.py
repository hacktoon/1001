# -*- encoding: utf-8 -*-
"""
Binary Heap
Autor:
    M. D. ATKINSON, J. R. SACK, N. SANTORO, and T. STROTHOTT
Colaborador:
    Juan Lopes (me@juanlopes.net)
Tipo:
    data-structures
Descrição:
    Implementação de priority queue usando uma binary min-heap.
    
Complexidade:  
    Inserção: O(log n) 
    Remoção: O(log n)
    Obter mínimo: O(1)
Dificuldade:
    Fácil
Referências: (opcional)
    http://en.wikipedia.org/wiki/Binary_heap
"""

class BinaryHeap:
    def __init__(self, V = []):
        self.V = [None] + list(V)
        self.heapify()
        
    def heapify(self):
        for i in range(self.count()/2, 0, -1):
            self.bubble_down(i)
        
    def count(self):
        return len(self.V) - 1
        
    def top(self):
        return (self.V[1] if self.count() > 0 else None)

    def push(self, value):
        self.V.append(value)
        self.bubble_up(self.count())
    
    def pop(self):
        if self.count() == 0: return None
        
        value = self.V[1]
        self.V[1] = self.V[-1]
        self.V.pop()
        self.bubble_down(1)
        return value
   
    def pop_all(self):
        while self.count() > 0:
            yield self.pop()
   
    def bubble_up(self, n):
        while n != 1 and self.less(n, n/2):
            self.swap(n, n/2)
            n /= 2
            
    def bubble_down(self, n):
        while self.less(n*2, n) or self.less(n*2+1, n):
            c = self.min(n*2, n*2+1)
            self.swap(n, c)
            n = c

    def less(self, a, b):
        if a>self.count(): return False
        if b>self.count(): return True
        return self.V[a]<self.V[b]
        
    def min(self, a, b):
        return (a if self.less(a,b) else b)
        
    def swap(self, a, b):
        self.V[a], self.V[b] = self.V[b], self.V[a]

heap = BinaryHeap()
heap.push(10)
heap.push(2)
heap.push(5)
heap.push(-100)
print heap.pop() #-100
print heap.pop() #2
print heap.pop() #5
print heap.pop() #10

print
print 'Heap sort'

V = [10, 2, 5, -100]
print V, '->', list(BinaryHeap(V).pop_all())
