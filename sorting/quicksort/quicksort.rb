
=begin
  Quicksort
Autor:
    ?
Colaborador:
    José Alberto O. Morais Filho (j.moraisg12@gmail.com)
Tipo:
    sorting
Descrição:
    Um dos melhores algoritmos de ordenação existente. Recebe um vetor, e, recursivamente, aplica a função Partition nos
  subvetores. A função partition reposiciona os valores de um array de tal forma que todos os elementos da esquerda do
  pivô (ultimo elemento) sejam menores que ele e os da direita sejam maiores.
Complexidade:
    O(n log n)
Dificuldade:
    médio
Referências:
    [1] Cormem, Thomas H. Introduction to Algorithms, 3rd Edition. (Páginas 170-174)
    [2] http://en.wikipedia.org/wiki/Quicksort
=end

# Entrada:
#   array = um vetor a ser ordenado;
#   left = primeira posição do vetor (ou subvetor);
#   right = última posição do vetor (ou subvetor);
# Saída:
#   o vetor ordenado

def partition(array, left, right)
  x = array[right]
  i = left - 1

  for j in left...right do
    if array[j] <= x then
      i += 1
      array[i], array[j] = array[j], array[i]
    end
  end

  array[i + 1], array[right] = array[right], array[i + 1]

  i + 1

end

def quicksort(array, left, right)

  if left < right then
    q = partition(array, left, right)
    quicksort(array, left, q - 1)
    quicksort(array, q + 1, right)
  end

end

# Exemplos
a = [2, 8, 7, 1, 3, 5, 6, 4]
b = [3, 1, 2, 6, 7, 4, 5]

quicksort a, 0, 7
print a

puts

quicksort b, 0, 6
print b
