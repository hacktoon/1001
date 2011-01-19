/*
Crivo de Eratóstenes
Autor:
    Eratóstenes (285-194 a.C.)
Colaborador:
    Filipe Saraiva (filip.saraiva@gmail.com)
Tipo:
    math
Descrição:
    Dado um número máximo, o Crivo de Eratóstenes encontra todos
    os números primos de 0 até este número máximo. 
Complexidade:
    O(n³)
Dificuldade:
    medio
Referências:
    [1] http://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes
    Licenca:
    GPLv3
*/

import java.util.ArrayList;

public class eratostenes {

	/**
	 * Crivo de Eratóstenes recebe a lista de todos os números de 2 até o número máximo,
	 * e o número máximo a ser verificado 
	 */
	public static ArrayList<Integer> eratostenes(ArrayList<Integer> lista, int numVerificacaoMax){
		
		/**
		 * A posição do primeiro número avaliado na lista é a posição 0
		 */
		int posicaoNumAvaliado = 0;
		int numAvaliado;
		
		/**
		 * Atenção! Aqui é criado um loop infinito proposital.
		 * 
		 * O mesmo só será terminado quando a condição dentro dele
		 * for atingida e a instrução *break* for executada. 
		 */
		while(true){
			
			/**
			 * Busca-se a posição do número que será avaliado
			 */
			while(lista.get(posicaoNumAvaliado) == 0){
				posicaoNumAvaliado++;
			}
			
			/**
			 * Inicialização do número avaliado
			 */
			numAvaliado = lista.get(posicaoNumAvaliado);
			
			/**
			 * Verificação dos números múltipos do número avaliado na lista
			 * 
			 * Caso o resto da divisão seja igual a 0, o número é múltiplo
			 * Então, o algoritmo substitui o valor do antigo número da lista por 0
			 */
			for(int contador = posicaoNumAvaliado + 1; contador < lista.size(); contador++){

				if((lista.get(contador) % numAvaliado) == 0){
					lista.set(contador, 0);
				}
			}
			
			/**
			 * Se o número que acabou de ser avaliado for igual ou maior que
			 * o número máximo a ser verificado, então o algoritmo termina sua execução 
			 */
			if(lista.get(posicaoNumAvaliado) >= numVerificacaoMax){
				break;
			}
			
			/**
			 * Caso o algoritmo não tenha terminado sua execução, incrementa-se posicaoNumAvaliado
			 * para que na próxima iteração se encontre o próximo número a ser avaliado
			 */
			posicaoNumAvaliado++;
			
		}
		
		ArrayList<Integer> listaPrimos = new ArrayList<Integer>();
		
		/**
		 * Esta instrução retira os números 0 da lista e coloca-se apenas os
		 * diferentes de 0 na na listaPrimos. Esta lista é o resultado do Crivo
		 * de Eratóstenes
		 */
		for(int contador = 0; contador < lista.size(); contador++){
		
			if(lista.get(contador) != 0){
				listaPrimos.add(lista.get(contador));
			}
		}
		
		return listaPrimos;
	}
	
	/**
    * Método main para executar o Crivo de Eratóstenes
    */
	public static void main(String[] args) {
		
		/**
		 * Lista que guardará os números entre 2 e o número limite máximo
		 * do algoritmo
		 */
		ArrayList<Integer> lista = new ArrayList<Integer>();
		
		/**
		 * Número limite máximo aleatório.
		 * Altere aqui para encontrar todos os números primos
		 * até ele!
		 */
		int numLimiteMax = 120;
		
		/**
		 * O número máximo a ser verificado é o piso da raiz quadrada
		 * do número limite máximo. Esta instrução encontra este número
		 */
		int numVerificacaoMax =  (int) Math.floor(Math.sqrt(numLimiteMax));
		
		/**
		 * Instrução para adicionar os números na lista que vai de 2 (o primeiro número primo)
		 * até o número limite máximo escolhido
		 */
		for(int contador = 2; contador <= numLimiteMax; contador++){
			lista.add(contador);
		}
		
		/**
		 * Captura do resultado do Crivo de Eratostenes
		 */
		ArrayList<Integer> listaPrimos = eratostenes(lista, numVerificacaoMax);
		
		/**
		 * Impressão do resultado do Crivo de Eratostenes
		 */
		for (Integer integer : listaPrimos) {
			System.out.print(integer + " ");
		}
		System.out.println();
	}

}
