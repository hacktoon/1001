/*
nums2words
Autor:
    ? 
Colaborador:
    Stanislaw Pusep 
Tipo:
    lang
Descrição:
    Conversor de números inteiros em strings de numerais cardinais em português.
    Exemplo:
        9223372036854775807 (maior inteiro positivo de 64 bits) => "nove quinqualhões e duzentos e vinte e três quatrilhões e trezentos e setenta e dois trilhões e trinta e seis bilhões e oitocentos e cinqüenta e quatro milhões e setecentos e setenta e cinco mil e oitocentos e sete"
Complexidade:
    ?
Dificuldade:
    medio
Referências: 
    [1] http://sysd.org/stas/node/20
    [2] http://pt.wikipedia.org/wiki/Nomes_dos_n%C3%BAmeros
    [3] http://pt.wikipedia.org/wiki/Escalas_curta_e_longa
*/

#include <malloc.h>
#include <stdio.h>
#include <string.h>

// tamanhos dos buffers
#define MAXRES_S		512
#define MAXTERN_S		64

// formato da estrutura da tabela de transição
typedef struct {
    unsigned int n;
    char *w;
} node;

/*
 * Expande blocos de milhares.
 * Os números maiores do que mil são "quebrados" em ternas que depois recebem um multiplicador.
 */
char *ext999 (unsigned int n) {
    unsigned int i, x, y;
    char *buf;
    // mapeamento número => nome
    node rel[] = {
        {900,	"novecentos"},	{800,	"oitocentos"},
        {700,	"setecentos"},	{600,	"seiscentos"},
        {500,	"quinhentos"},	{400,	"quatrocentos"},
        {300,	"trezentos"},	{200,	"duzentos"},
        {100,	"cento"},	    {90,	"noventa"},
        {80,	"oitenta"},	    {70,	"setenta"},
        {60,	"sessenta"},	{50,	"cinquenta"},
        {40,	"quarenta"},	{30,	"trinta"},
        {20,	"vinte"},	    {19,	"dezenove"},
        {18,	"dezoito"},	    {17,	"dezessete"},
        {16,	"dezesseis"},	{15,	"quinze"},
        {14,	"quatorze"},	{13,	"treze"},
        {12,	"doze"},	    {11,	"onze"},
        {10,	"dez"},		    {9,	    "nove"},
        {8,	    "oito"},	    {7,	    "sete"},
        {6,	    "seis"},	    {5,	    "cinco"},
        {4,	    "quatro"},	    {3,	    "três"},
        {2,	    "dois"},	    {1,	    "um"},
    };

    buf = (char *) malloc(MAXTERN_S);
    buf[0] = '\0';

    // casos especiais
    if (!n) {
        strcpy(buf, "zero");
        return buf;
    } else if (n == 100) {
        strcpy(buf, "cem");
        return buf;
    }

    // faz a redução do número fatorando pelos índices do mapeamento
    while (n) {
        for (i = 0; i < sizeof(rel); i++) {
            x = rel[i].n;
            y = n % x;
            if (x + y == n) {
                n = y;
                strcat(buf, rel[i].w);
                if (n)
                    strcat(buf, " e ");
                break;
            }
        }
    }

    return buf;
}

char *nums2words (long n) {
    unsigned long x;
    unsigned int y;

    int i, j, k;
    char *res, *p;

    // mapeamento dos multiplicadores para inteiros 'signed' de 64 bits
    char *ord[] = {
        NULL,		    NULL,
        "mil",		    "mil",
        "milhão",  	    "milhões",
        "bilhão",	    "bilhões",
    	"trilhão",	    "trilhões",
       	"quatrilhão",	"quatrilhões",
        "quinqualhão",  "quinqualhões",
    };
    // array para armazenamento das ternas pré-processadas
    unsigned int tern[(sizeof(ord) / sizeof(char *)) / 2];

    res = (char *) malloc(MAXRES_S);
    res[0] = '\0';

    // trata números negativos
    if (n < 0) {
        n *= -1;
        strcat(res, "menos ");
    }

    if (n < 1000) {
        // números menores do que mil: caso mais simples
        strcat(res, ext999(n));
    } else {
        // quebra o número em ternas
        x = n;
        for (j = 0; x; j++) {
            y = x % 1000;
            x /= 1000;

            tern[j] = y;
        }

        // obtém string para cada terna e concatenta no resultado
        for (i = j - 1; i >= 0; i--) {
            if (y = tern[i]) {
                // concatena a respectiva terna
                p = ext999(y);
                strcat(res, p);
                free(p);

                // trata singular ou plural do multiplicador
                k = i * 2;
                if (y != 1)
                    k++;

                // concatena o multiplicador
                if (p = ord[k]) {
                    strcat(res, " ");
                    strcat(res, p);
                }

                // nem sempre o 'e' é necessário; porém desconheço a regra correta :(
                strcat(res, " e ");
            }
        }
        res[strlen(res) - 3] = '\0';
    }

    return res;
}


int main (void) {
    long n;
    char *p;

    do {
        printf("Digite um número (0 para sair): ");
        scanf("%ld", &n);
        fflush(stdin);

        p = nums2words(n);
        printf("você digitou \"%s\"\n", p);
        free(p);
    } while (n);

    return 0;
}
