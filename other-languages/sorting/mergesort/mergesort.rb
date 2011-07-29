
=begin
  Mergesort
Autor:
    ?
Colaborador:
    José Alberto O. Morais Filho (j.moraisg12@gmail.com)
Tipo:
    sorting
Descrição:
    Um dos melhores algoritmos de ordenação existente. Recebe um vetor, e, recursivamente, aplica a função Merge nos
  subvetores. A função merge recebe dois subvetores e os agrupa em um array ordenado.
Complexidade:
    O(n log n)
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
    if l[i] <= r[j] then
      array[k] = l[i]
      i += 1
    else
      array[k] = r[j]
      j += 1
    end
  end
end

def mergesort(array, left, right)
  if left < right then
    mid = (left + right) / 2
    mergesort(array, left, mid)
    mergesort(array, mid + 1, right)
    merge(array, left, mid, right)
  end
end

a = [5, 3, 4, 1, 9, 7, 2, 6, 8]
mergesort(a, 0, 8)
print a

puts

b = [8, 1, 3, 2, 5, 7, 6, 4]
mergesort(b, 0, 7)
