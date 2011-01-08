=begin
Bozosort
Autor:
    Bozo
Tipo:
    sorting
Descrição:
    Embaralha um vetor indefinidamente, até que os números estejam em ordem.
Complexidade:  
    Pior caso: O(infinito)
    Melhor caso: O(n)
Dificuldade:
    facil
Referências:
    http://nerdson.com/blog/libbozo-01/
    http://pt.wikipedia.org/wiki/Bogosort
=end

class Array
  def bozosort
    list = self.sort
    while self != list
      self.shuffle!
    end
    self
  end
end 

require 'test/unit'
require 'lib/bozosort'

class TestBozosort < Test::Unit::TestCase
  def test_bozosort
    randon_array = Array.new(rand(20)).map{rand(99999999)}
    sorted_array = randon_array.sort
    assert_equal randon_array.bozosort, sorted_array
  end
end
