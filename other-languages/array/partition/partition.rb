
=begin
  Partition
Autor:
    ?
Colaborador:
    José Alberto O. Morais Filho (j.moraisg12@gmail.com)
Tipo:
    array-operations
Descrição:
    Reposiciona os valores de um array de tal forma que todos os elementos da esquerda do pivô (ultimo elemento) sejam
  menores que ele e os da direita sejam maiores.
Complexidade:
    O(n)
Dificuldade:
    médio
Referências:
   [1] Cormem, Thomas H. Introduction to Algorithms, 3rd Edition. (Páginas 171-172)
=end

# Entrada:
#   array = um vetor a ser reposicionado;
#   left = primeira posição do vetor (ou subvetor);
#   right = última posição do vetor (ou subvetor);
# Saída:
#   A posição do pivô no novo vetor

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

# Exemplos
a = [2, 8, 7, 1, 3, 5, 6, 4]
b = [3, 1, 2, 6, 7, 4, 5]

print(partition a, 0, 7)
puts
print(partition b, 0, 6)or (ou subvetor);
#   right = última posição do vetor (ou subvetor);
# Saída:
#   A posição do pivô no novo vetor

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

# Exemplos
a = [2, 8, 7, 1, 3, 5, 6, 4]
b = [3, 1, 2, 6, 7, 4, 5]

print(partit