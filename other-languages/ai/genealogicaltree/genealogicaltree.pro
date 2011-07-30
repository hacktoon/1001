/*
Árvore Genealógica
Autor:
    ???
Colaborador:
    Filipe Saraiva (filip.saraiva@gmail.com)
Tipo:
    ai
Descrição:
    Implementação de uma árvore genealógica em
    Prolog. Teste do mecanismo de inferência da
    linguagem.
Complexidade:
    ???
Dificuldade:
    médio
Referências:
    [1] Palazzo, L. Introdução à Programação Prolog, Editora da
	Universidade Católica de Pelotas, Pelotas, 1997.
*/

/*
 * Este código serve para apresentar os rudimentos da inferência
 * lógica da linguagem Prolog. Nele, criamos uma árvore genealógica
 * e, a partir da base de dados ("fatos"), conseguiremos extrair
 * conhecimento não disponível anteriormente.
 */

/*
 * Fatos - Base de Dados
 */
pai(raimundo, ana).
pai(raimundo, renata).
pai(raimundo, lucio).

pai(estevao, marcelo).
pai(estevao, pamela).

pai(henrique, filomena).

mae(marcela, ana).
mae(marcela, renata).

mae(sofia, lucio).

mae(clarisse, marcelo).
mae(clarisse, pamela).

mae(sofia, filomena).

masculino(raimundo).
masculino(estevao).
masculino(henrique).
masculino(lucio).
masculino(marcelo).

feminina(marcela).
feminina(sofia).
feminina(clarisse).
feminina(ana).
feminina(renata).
feminina(pamela).
feminina(filomena).

/*
 * Predicados
 */

% Verifica quais pessoas tem o mesmo pai e a mesma mãe de uma
% pessoa "X". Estas são "irmãos total".
irmaostotal(X, Z) :- pai(Y, X), mae(K, X), pai(Y, Z), mae(K, Z).
