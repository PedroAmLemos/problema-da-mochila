#include <stdio.h>
#include <time.h>
#include <stdlib.h>
int g;

int max(int a, int b){	return (a > b) ? a : b; }

int brute_force(int capacidade, int pesos[], int variaveis[], int nVariaveis, time_t start_time)
{
	time_t now = time(0);
	if(now - start_time < 10){
		if (nVariaveis == 0 || capacidade == 0)
			return 0;
		if (pesos[nVariaveis - 1] > capacidade){
			g = brute_force(capacidade, pesos, variaveis, nVariaveis - 1, start_time);
			return g;
		}
		else{
			g = max(variaveis[nVariaveis - 1] + brute_force(capacidade - pesos[nVariaveis - 1], pesos, variaveis, nVariaveis - 1, start_time), brute_force(capacidade, pesos, variaveis, nVariaveis - 1, start_time));
			return g;
		}
	}
	return 0;
}

int limitante(int capacidade, int pesos[], int variaveis[], int nVariaveis)
{
	int k, j;
	/*int tabela[n + 1][W + 1];*/
	int **tabela = (int **) malloc((nVariaveis+1)*sizeof(int *));
	for (int i = 0; i < (nVariaveis+1); i++) {
		tabela[i] = (int *) malloc((capacidade+1)*sizeof(int));
	}
	for (k = 0; k <= nVariaveis; k++)
	{
		for (j = 0; j <= capacidade; j++)
		{
			if (k == 0 || j == 0)
				tabela[k][j] = 0;
			else if (pesos[k - 1] <= j)
				tabela[k][j] = max(variaveis[k - 1] + tabela[k - 1][j - pesos[k - 1]], tabela[k - 1][j]);
			else
				tabela[k][j] = tabela[k - 1][j];
		}
	}
	return tabela[nVariaveis][capacidade];
}

int soma(int vetor[], int n){
	int i = 0;
	for(int k = 0; k < n; k++){
		i += vetor[k];
	}
	return i;  
}

int maior(int vetor[]){
	int i = 0;
	for(int k=0; k < sizeof(*vetor); k++){
		if(vetor[k]>i){
			i = vetor[k];
		}
	}
	return i;
}


int main()
{
	int random_number;
	time_t start_time = time(0);
	int variaveis[10];
	int pesos[10];
	for (int i = 0; i < 10; i++) {
		random_number = rand() % 350;
		variaveis[i] = random_number;
		random_number = rand() % 350;
		pesos[i] = random_number;
	}
	int capacidade;
	int n = sizeof(variaveis) / sizeof(variaveis[0]);
	int resSoma = soma(pesos, n);
	if(resSoma/2 < maior(pesos)){
		capacidade = resSoma/2 + maior(pesos);
	}else{
		capacidade = resSoma/2;
	}
	brute_force(capacidade, pesos, variaveis, n, start_time);
	printf("Brute Force:\tResultado de uma mochila com capacidade %d e %d variaveis, foi: %d\n", capacidade, n, g);
	printf("Uso de limi:\tResultado de uma mochila com capacidade %d e %d variaveis, foi: %d\n", capacidade, n, limitante(capacidade, pesos, variaveis, n));
	return 0;
}

