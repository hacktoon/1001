
"""
Stack
Autor:
    ?
Colaborador:
    Guido Luz Percú (guidopercu@gmail.com)
Tipo:
    data-structures
Descrição:
    Implementação da estrutura de dados Stack, uma coleção de elementos com duas
    operações principais: push e pop. Também conhecida por LIFO (last in, first
    out).
Complexidade:
    ?
Dificuldade:
    facil
Referências: (opcional)
    http://www.wikiwand.com/en/Stack_%28abstract_data_type%29
"""


class Stack:
    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        return "{}".format(self._stack)

    def top(self):
        return self._stack[-1]

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        self._stack.pop()


if __name__ == "__main__":
    pilha = Stack()
    pilha.push(1)
    pilha.push(2)
    pilha.push(3)
    print(pilha)
    print(pilha.top())
    print("Tamanho da pilha: {}".format(len(pilha)))

    pilha.pop()
    print(pilha)
    print("Tamanho da pilha: {}".format(len(pilha)))
    print(pilha.top())
