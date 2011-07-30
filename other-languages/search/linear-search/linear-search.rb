
=begin
  Linear Search
Autor:
    ?
Colaborador:
    José Alberto O. Morais Filho (j.moraisg12@gmail.com)
Tipo:
    search
Descrição:
    Utiliza força bruta em um array para retornar a posição de um valor nesse array, ou retornar -1, se nada
  for encontrado.
Complexidade:
    O(n)
Dificuldade:
    fácil
=end

# Entrada:
#   array = vetor onde o valor será pesquisado
#   search = valor procurado
# Saída:
#   a posição da primeira ocorrência do valor, ou -1, caso o valor não for encontrado

def linear_search(array, search)
  array.each_index {|i| return i if array[i] == search}
  -1
end

# Exemplos

a = [1,5, 6, 3, 7,4]

print linear_search(a, 6)
print linear_search(a, 60)

