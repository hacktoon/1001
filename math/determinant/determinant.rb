
=begin
  Matrix Determinant
Autor:
    ?
Colaborador:
    José Alberto O. Morais Filho (j.moraisg12@gmail.com)
Tipo:
    math
Descrição:
    Utiliza a decomposição LU para calcular o determinante da matriz. A decomposição LU gera duas matrizes triangulares,
  de forma que A = L * U -> det(A) = det(L) * det(U).
Complexidade:
    O(n^3)
Dificuldade:
    médio
Referências:
   [1] http://en.wikipedia.org/wiki/LU_decomposition
   [2] http://en.wikipedia.org/wiki/Determinant
=end

# Entrada:
#   a = uma matriz quadrada
# Saída:
#   o determinante dessa matriz

def lu_decompose(a)

  n = a.length

  for i in 0..n-1 do
    for j in 0..n-1 do
      a[i][j] = a[i][j].to_f
    end
  end

  u = Array.new(n) {Array.new(n) {0}}
  l = Array.new(n) {Array.new(n) {0}}

  for i in 0..n-1 do
    for j in 0..n-1 do
      l[i][i] = 1 if i == j
    end
  end

  for k in 0..n-1 do

    u[k][k] = a[k][k]

    for i in k+1..n-1 do
      l[i][k] = a[i][k] / u[k][k]
      u[k][i] = a[k][i]
    end

    for i in k+1..n-1 do
      for j in k+1..n-1 do
        a[i][j] = a[i][j] - l[i][k]*u[k][j]
      end
    end

  end

  return l, u

end

def determinant(a)

  n = a.length
  l, u = lu_decompose(a)
  
  det = 1
  for i in 0..n-1 do
    det *= u[i][i]
  end

  det

end

# Exemplos
a = [[1, 3, 2], [9, 5, 4], [8, 6, 7]]
b = [[4, 3, 8, 4], [12, 1, 9, 13], [5, 14, 2, 10], [6, 16, 7, 11]]

print(determinant a)
puts
print(determinant b)
