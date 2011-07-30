--[[
	Fibonacci recursivo e iterativo
Autor:
    Fibonacci
Colaborador:
    José Ivan Bezerra Vilarouca Filho (ivanfilho2204@hotmail.com)
Tipo:
    math
Descrição:
    Algoritmo usado para gerar a sequência de Fibonacci.
	Um termo é a soma de seus 2 antecessores. Sendo os primeiros
	dois termos com valores 0 e 1 respectivamente.
	0, 1, 2, 3, 5, 8, 13, ...
Complexidade:  
    O(n)
Dificuldade:
    facil
]]--

function fibonacci_recursivo(ntermos)

	if (ntermos < 1) then
	
		return;
	elseif (ntermos == 1) then
	
		return 0;
	elseif (ntermos == 2) then
	
		return 1;
	end
	
	return fibonacci_recursivo(ntermos - 1) + fibonacci_recursivo(ntermos - 2);
end

function fibonacci_iterativo(ntermos)

	if (ntermos < 1) then
	
		return;
	elseif (ntermos == 1) then
	
		return 0;
	elseif (ntermos == 2) then
	
		return 1;
	end
	
	local ante1, ante2, i = 0, 1, 3;
	while (i <= ntermos) do
	
		ante1, ante2 = ante2, ante1 + ante2;
		i = i + 1;
	end
	
	return ante2;
end

j = 1;
while (j <= 15) do

	io.write(fibonacci_recursivo(j) .. " ");
	j = j + 1;
end

print("");

j = 1;
while (j <= 15) do

	io.write(fibonacci_iterativo(j) .. " ");
	j = j + 1;
end
