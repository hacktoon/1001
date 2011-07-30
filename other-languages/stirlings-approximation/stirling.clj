(defn stirling [n]
  "
  Fórmula de Stirling
  
  Autor:
    Pedro Menezes <eu@pedromenezes.com>
    DiogoK <diogo@diogok.net>
  Tipo:
    math
  Descrição:
    A Fórmula de Stirling estabelece uma aproximação assintótica para o fatorial de um número.
  Referências:
    http://pt.wikipedia.org/wiki/F%C3%B3rmula_de_Stirling
  "
  (* (Math/sqrt (* 2 Math/PI n)) (Math/pow (/ n Math/E) n)))
  
(dorun (for [n (range 1 10)] 
  (println "fat" n "~" (stirling n))
))