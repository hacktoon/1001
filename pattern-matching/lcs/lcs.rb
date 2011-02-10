# LCS (Longest Common Subsequence)
# Autor:
#   ?
# Colaborador:
#   Luiz Fernando Oliveira Corte Real <luiz@vidageek.net>
# Tipo:
#   pattern-matching
# Descrição:
#   Este algoritmo calcula a maior string que subsequência de outras duas,
#   chamada de subsequência comum máxima ou, em inglês, longest common
#   subsequence (LCS).
#
#   Por exemplo, dada a string 'banana' e a string 'abacate', a maior string
#   que é substring das duas é 'baa', que pode ser encontrada se pegarmos a
#   primeira (b), a segunda (a) e quarta letra (a) da palavra 'banana', ou a
#   segunda (b), a terceira (a) e a quinta letra (a) da palavra 'abacate'.
#
#   O algoritmo baseia-se em programação dinâmica para calcular, primeiro,
#   o tamanho da maior substring das duas strings dadas. Ele faz isso
#   colocando, na matriz lcs_matrix, o tamanho da maior substring das duas até
#   certo ponto. Ou seja, na posição [i, j] da matriz teremos o tamanho da
#   LCS das strings string1[1..i] e string2[1..j] (os primeiros i caracteres
#   da string1 e os primeiros j caracteres da string2). O algoritmo vai
#   preenchendo essa matriz pelas linhas, com base nas strings e numa
#   fórmula de recorrência. No fim, o tamanho da LCS das duas strings estará
#   na última posição preenchida da matriz.
#
#   Para recuperar qual é essa LCS, o algoritmo percorre a matriz procurando
#   quais foram as posições das strings que fizeram o tamanho ser
#   incrementado.
# Complexidade:
#   O(nm), onde n e m são os tamanhos das strings dadas
# Referências:
#   http://en.wikipedia.org/wiki/Longest_common_subsequence_problem
# Licença:
#   BSD

class LCS
  def initialize(string1, string2)
    @string1 = string1
    @string2 = string2
  end

  def length
    @lcs_matrix ||= compute_lcs_matrix
    return @lcs_matrix[@string1.size][@string2.size]
  end

  def string
    return '' if @string1.empty? or @string2.empty?
    @lcs_matrix ||= compute_lcs_matrix
    @lcs_string ||= find_lcs_in_matrix
    return @lcs_string
  end

  private
  def compute_lcs_matrix
    counting = []
    (@string1.size+1).times { counting << Array.new(@string2.size+1, 0) }
    @string1.size.times do |i|
      @string2.size.times do |j|
        if @string1[i] == @string2[j]
          counting[i+1][j+1] = counting[i][j] + 1
        else
          counting[i+1][j+1] = [counting[i+1][j], counting[i][j+1]].max
        end
      end
    end
    return counting
  end

  def find_lcs_in_matrix
    return recursive_find_lcs_in_matrix(@string1.size, @string2.size)
  end

  def recursive_find_lcs_in_matrix(i, j)
    return '' if i == 0 or j == 0
    if @string1[i-1] == @string2[j-1]
      return recursive_find_lcs_in_matrix(i-1, j-1) + @string1[i-1].chr
    end
    if @lcs_matrix[i][j-1] > @lcs_matrix[i-1][j]
      return recursive_find_lcs_in_matrix(i, j-1)
    end
    return recursive_find_lcs_in_matrix(i-1, j)
  end
end

###################################################
# Exemplos de uso, com resultados esperados ao lado
###################################################

puts LCS.new('a string', 'another string').string # 'a string'
puts LCS.new('yes', 'not').length                 # 0
puts LCS.new('french', 'trench').string           # 'rench'
