/*
# -*- coding: utf-8 -*-

"""
Backtracking e Heurísticas aplicadas para se resolver um sudoku.
A busca é feita no grafo de estados do problema
Autores: 
    ? 
Colaborador:
 	Péricles Lopes Machado [gogo40] (pericles.raskolnikoff.gmail.com)
Tipo: 
    search
Descrição: 
    Sudokus são problema NP-difíceis, por isso na maior parte
do tempo procuramos heurísticas que acelerem a busca. Nesse código
são implementadas algumas heurísticas humanas, como limitar as opções
de jogada em cada estado usando as regras do jogo.
	Existe uma solução mais eficiente utilizando-se o algoritmo X[5].
Futuramente, planejo implementar essa outra abordagem. Este código
é apenas um exemplo de como heurísticas podem acelerar a busca de uma solução de sudoku.

Complexidade: 
    O(2^N)
Dificuldade: 
    Difícil
Referências:
    [1] http://en.wikipedia.org/wiki/Backtracking
    [2] http://en.wikipedia.org/wiki/Heuristic
	[3] http://falapericles.blogspot.com.br/2009/05/grafo-de-estados-e-suas-aplicacoes.html
	[4] http://webdocs.cs.ualberta.ca/~games/Sokoban/
	[5] http://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X
"""
*/


/*
Para testar o código pode-se utilizar o seguinte problema do SPOJ brasil:

http://br.spoj.com/problems/BSUDO/

Ou digitar no terminal a seguinte entrada (test_001.in):
1
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107

O '0' representa uma posição vaga na grade

Este algoritmo é bem eficiente para o caso 9x9, mas para o caso 16x16 ainda é preciso melhorias.
O algoritmo X do Knuth é mais eficiente, mas é um pouco mais complexo.
*/
#include <stdio.h>

#define INF 500

using namespace std;


/*vetor de palavras com tamanho menor que 32 bits**/
typedef long long lint;
typedef unsigned long long ulint;

/*Esta estrtura representa um nó no grafo de estados do problema*/
struct V{
	//tam_word=9  NMAX=20;
	//n_words=64/9 numero de palavras por chunck
	
	int n_words, nbits, MASK;
	
	ulint v[6];
	ulint mask;
	
	V(int n_words=5,int nbits=10, int MASK=1023)
	:n_words(n_words),nbits(nbits),mask(MASK){
		for(int i=0;i<6;i++) v[i]=0;
	}
	
	V(const V& b){
		n_words=b.n_words; nbits=b.nbits;
		MASK=b.MASK; mask=b.mask;
		for(int i=0;i<6;i++) v[i]=b.v[i];
	}
	
	inline
	void insert(int p, ulint V){
		int i;
		
		i=p/n_words;
		p=p%n_words;
		
		p*=nbits;
		
		v[i]=(v[i]^(v[i] & (mask<<p))) | (V<<p);
	}
	
	inline
	int get(int p){
		int i;
		
		i=p/n_words;
		p=p%n_words;
		p*=nbits;
		
		return (int)((v[i]>>p)&mask);
	}
	
	V& operator=(const V& b){
		n_words=b.n_words; nbits=b.nbits;
		MASK=b.MASK;  mask=b.mask;
		for(int i=0;i<6;i++) v[i]=b.v[i];
		return *this;
	}

};

/****************************/


//Armazena estado anterior
struct st{
	V s, pl, pc, ps;//estado anterior
	int le, x, y;//ultima escolha e posicao onde ocorreu
	
	st():s(16,4,15),pl(),pc(),ps(),le(1),x(0),y(0){}
	
	st(const V& s, const V& pl, const V& pc, const V& ps, int le=1, int x=0, int y=0)
	:s(s),pl(pl),pc(pc),ps(ps),le(le),x(x),y(y){}
	
	st& operator=(const st& a){
		s=a.s; pl=a.pl; pc=a.pc; ps=a.ps;
		le=a.le; x=a.x; y=a.y;
		return *this;
	}
};


/*Pilha de estados*/
static st Q[81];
int ip;
static int hel[10];
static int lg[1<<10];
static int ones[1<<10];
static const ulint inf=~(0LL);

// Imprime solução
inline
void print(V& sol)
{
	int i, j;
	for(i=0;i<9;i++){
		for(j=0;j<9;j++) printf("%d",sol.get(i*9+j));
		printf("\n");
	}
}

/*Função de backtracking que explora a arvore de possibilidades do jogo*/

bool solve(V& s){
	V podeLin, podeCol, podeSet;
	int i, j, x, y, a, b, set;
	int px, py, mi, l, ns;
	bool ok;
	
	for(i=0;i<2;i++) podeCol.v[i]=podeSet.v[i]=podeLin.v[i]=inf;
	
	ok=true;
	ip=0;
	int np=0;
	for(;;){
	
		//Verifica se já resolvi o sudoku s
		//print(s);
		init:
		np++;
		//Caso não foi possível realizar uma jogada na iteração anterior desempilha-se um estado da pilha
		if(!ok)
			for(;;){
				ip--;
				
				if(ip==-1) return false;
				else{
					s=Q[ip].s;
					podeLin=Q[ip].pl; podeCol=Q[ip].pc; podeSet=Q[ip].ps;
					px=i=Q[ip].x; py=j=Q[ip].y;
					
					a=(i/3); b=(j/3); set=a*3+b;
					y=podeLin.get(i); y&=podeCol.get(j); y&=podeSet.get(set); 
					
					for(i=Q[ip].le+1;i<10;i++)
						if((y>>i)&0x1){
							Q[ip]=st(s,podeLin,podeCol,podeSet,i,px,py);
							ip++;
							s.insert(px*9+py,i);
							goto cont;//Preciso sair desse mais aninhado
						}
				}
			}
		
		cont:
		
		//Realiza travas  e procura posições que tem opcoes unicas
		ns=0;
		for(i=0;i<9;i++)
			for(j=0;j<9;j++){
				x=s.get(i*9+j);
				a=(i/3); b=(j/3); set=a*3+b;
					
				if(x>0){
					ns++;
					//Atualiza linha
					y=podeLin.get(i); y&=hel[x]; podeLin.insert(i,y);
					//Atualiza coluna
					y=podeCol.get(j); y&=hel[x]; podeCol.insert(j,y);
					//Atualiza setor
					y=podeSet.get(set); y&=hel[x]; podeSet.insert(set,y);
				}
			}
		
		
		if(ns==81){ print(s);  return true; }
		
		/* Atualiza opções para cada linha e coluna*/
		mi=INF; ok=false;
		for(i=0;i<9;i++)
			for(j=0;j<9;j++){	
				x=s.get(i*9+j);
				a=(i/3); b=(j/3); set=a*3+b;
					
				if(x==0){
					y=podeLin.get(i); y&=podeCol.get(j); y&=podeSet.get(set); 
					x=lg[y];
					if(x>0){
						/*Insere possivel valor pra posição i, j da grade*/
						s.insert(i*9+j,x);
						/*bloqueia x como opção para linha i, coluna j e setor set*/
						y=podeLin.get(i); y&=hel[x]; podeLin.insert(i,y);
						y=podeCol.get(j); y&=hel[x]; podeCol.insert(j,y);
						y=podeSet.get(set); y&=hel[x]; podeSet.insert(set,y);
						ok=true;
					}else if(y==0)  goto init; 
					else{
						/*opções pra pra posição i, j*/
						x=ones[y]; 
						if(x<mi){ mi=x; l=y; px=i; py=j; }
					}
				}
			}
		
		/*Caso não foi possível realizar um movimento nesse laço empilha-se todas opções
		disponíveis e tenta-se qual delas gera uma solução válida*/
		if(!ok){
			i=px; j=py; a=(i/3); b=(j/3); set=a*3+b;
			y=podeLin.get(i); y&=podeCol.get(j); y&=podeSet.get(set); 
			
			for(i=1;i<10;i++)
				if((y>>i)&0x1){
					Q[ip]=st(s,podeLin,podeCol,podeSet,i,px,py);
					ip++;
					s.insert(px*9+py,i);
					ok=true;
					break;
				}
		}
	}
}

//*********************************************************//
//MAIN
//*********************************************************//

/*Verifica é possivel resolver a grade*/
bool find_error(V& s){
	for(int n=1;n<10;n++){
		int noc;
		for(int i=0;i<9;i++){
			noc=0;
			for(int j=0;j<9;j++)
				if(s.get(i*9+j)==n) noc++;
			if(noc>1) return false;
		}
		
		for(int i=0;i<9;i++){
			noc=0;
			for(int j=0;j<9;j++)
				if(s.get(j*9+i)==n) noc++;
			if(noc>1) return false;
		}
		
		for(int i=0;i<3;i++){
			int lm=3*(i+1);
			int auxI=3*i;
			
			for(int j=0;j<3;j++){
				int lp=3*(j+1);
				noc=0;
				
				for(int m=auxI;m<lm;m++)
					for(int p=3*j;p<lp;p++){
						int x=s.get(m*9+p);
						if(x==n) noc++;
					}
				if(noc>1) return false;
			}	
		}
		
	}
	return true;
}

int main()
{
	int N, x, i, j, len, m,c;
	V s(16,4,15);
	
	len=1<<10; m=len-1;
	for(i=0;i<len;i++) {
		lg[i]=-1;
		x=0;
		for(j=0;j<10;j++)
			if(i>>j & 0x1)x++;
		ones[i]=x;
	}
	
	for(i=0;i<10;i++)  { 
		lg[1<<i]=i;
		hel[i]=m-(1<<i);
		if(i>0) hel[i]--;
	}
	
	c=1;
	scanf("%d",&N);
	while(N--){
		for(i=0;i<9;i++)
			for(j=0;j<9;j++){
				scanf("%1d",&x);
				s.insert(i*9+j,x);
			}
		
		if(!find_error(s)) printf("Could not complete this grid.\n");
		else if(!solve(s)) printf("Could not complete this grid.\n");
		c++;
	}
	return 0;
}



