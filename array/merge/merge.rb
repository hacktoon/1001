
=begin
  Merge
Autor:
    ?
Colaborador:
    José Alberto O. Morais Filho (j.moraisg12@gmail.com)
Tipo:
    array-operations
Descrição:
    Combina dois subvetores (ordernados), gerando um vetor ordenado
Complexidade:
    O(n)
Dificuldade:
    médio
Referências:
   [1] Cormem, Thomas H. Introduction to Algorithms, 3rd Edition. (Páginas 29-34)
=end

def merge(array, left, mid, right)
  n1 = mid - left + 1
  n2 = right - mid

  l = Array.new(n1 + 1) {0}
  r = Array.new(n2 + 1) {0}

  for i in 0...n1 do
    l[i] = array[left + i]
  end

  for j in 1..n2 do
    r[j - 1] = array[mid + j]
  end

  l[n1] = 999999
  r[n2] = 999999

  i = 0
  j = 0

  for k in left..right do
    if l[i] <= r[j]
      array[k] = l[i]
      i += 1
    else
      array[k] = r[j]
      j += 1
    end
  end
end

# Exemplos

a = [5, 6, 7, 8, 9, 1, 2, 3, 4]
merge(a, 0, 4, 8)
print a

puts

b = [1, 3, 5, 7, 2, 4, 6, 8]
merge(b, 0, 3, 7)
print b = right - mid

  l = Array.new(n1 + 1) {0}
  r = Array.new(n2 + 1) {0}

  for i in 0...n1 do