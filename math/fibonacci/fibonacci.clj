(comment 
Cálculo da sequência de Fibonacci
Autor 
    ? 
Colaborador
    Guilherme Victal (guilhermevictal em gmail.com) 
Tipo
    math
Descrição 
    Cálculo do n-ésimo valor da sequência de fibonacci recursivamente,
    a partir da definição [a[n]=a[n-1] + a[n-2], a[0]=a[1]=1]
    Na prática é muito lento mesmo para n não muito grande;
Complexidade
  ? 
Dificuldade
  facil
)


(defn fibonacci [n]
  (if (< n 2)
    1
    (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))


(println (map fibonacci (range 1 20)))

