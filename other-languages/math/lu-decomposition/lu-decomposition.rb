
=begin
  LU Decomposition
Autor:
    ?
Colaborador:
    José Alberto O. Morais Filho (j.moraisg12@gmail.com)
Tipo:
    math
Descrição:
    Fatora uma matriz não singular em duas matrizes triangulares, uma superior (upper) e uma inferior (lower). É
  utilizado para facilitar resoluções de sistemas de equações lineares ou o cálculo de determinates.
Complexidade:
    O(n^3)
Dificuldade:
    medio
Referências:
   [1] http://en.wikipedia.org/wiki/LU_decomposition
   [2] Cormem, Thomas H. Introduction to Algorithms, 3rd Edition. (Páginas 819-822)
=end

# Entrada:
#   a = array a ser fatorado
# Saída:
#   dois arrays, l e u

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

# Exemplos
a = [[1, 3, 2], [9, 5, 4], [8, 6, 7]]
l, u = lu_decompose(a)
print "L: #{l}, U: #{u}"

puts

b = [[4, 3, 8, 4], [12, 1, 9, 13], [5, 14, 2, 10], [6, 16, 7, 11]]
l, u = lu_decompose(b)
print "L: #{l}, U: #{u}"

