import java.util.ArrayList;

public class eratostenes {

	public static ArrayList<Integer> eratostenes(ArrayList<Integer> lista, int numVerificacaoMax){
		
		int posicaoNumAvaliado = 0;
		int numAvaliado;
		
		while(true){
			
			while(lista.get(posicaoNumAvaliado) == 0){
				posicaoNumAvaliado++;
			}
			
			numAvaliado = lista.get(posicaoNumAvaliado);
			
			for(int contador = posicaoNumAvaliado + 1; contador < lista.size(); contador++){

				if((lista.get(contador) % numAvaliado) == 0){
					lista.set(contador, 0);
				}
			}
			
			if(lista.get(posicaoNumAvaliado) >= numVerificacaoMax){
				break;
			}
			
			posicaoNumAvaliado++;
			
		}
		
		ArrayList<Integer> listaPrimos = new ArrayList<Integer>();
		
		for(int contador = 0; contador < lista.size(); contador++){
		
			if(lista.get(contador) != 0){
				listaPrimos.add(lista.get(contador));
			}
		}
		
		return listaPrimos;
	}
	
	public static void main(String[] args) {
		
		ArrayList<Integer> lista = new ArrayList<Integer>();
		
		int numLimiteMax = 120;
		
		int numVerificacaoMax =  (int) Math.floor(Math.sqrt(numLimiteMax));
		
		for(int contador = 2; contador <= numLimiteMax; contador++){
			lista.add(contador);
		}
		
		ArrayList<Integer> listaPrimos = eratostenes(lista, numVerificacaoMax);
		
		for (Integer integer : listaPrimos) {
			System.out.print(integer + " ");
		}

	}

}
