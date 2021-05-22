#include <stdio.h>
#include <time.h>
#include <stdlib.h>


// A utility function that returns
// maximum of two integers
int max(int a, int b)
{
	return (a > b) ? a : b;
}

// Returns the maximum value that
// can be put in a knapsack of capacity W
int mochila_limitantes(int W, int wt[], int val[], int n)
{
	int i, w;
	/*int tabela[n + 1][W + 1];*/
	int **tabela = (int **) malloc((n+1)*sizeof(int *));
	for (int k = 0; k < (n+1); k++) {
		tabela[k] = (int *) malloc((W+1)*sizeof(int));
	}

	// Build table K[][] in bottom up manner
	for (i = 0; i <= n; i++)
	{
		for (w = 0; w <= W; w++)
		{
			if (i == 0 || w == 0)
				tabela[i][w] = 0;
			else if (wt[i - 1] <= w)
				tabela[i][w] = max(val[i - 1]
						+ tabela[i - 1][w - wt[i - 1]],
						tabela[i - 1][w]);
			else
				tabela[i][w] = tabela[i - 1][w];
		}
	}

	return tabela[n][W];
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

// Driver Code
int main()
{
	srand(time(NULL));
	int random_number;
	int variaveis[1000];
	int pesos[1000];
	for (int i = 0; i < 1000; i++) {
		random_number = rand() % 3500;
		variaveis[i] = random_number;
		random_number = rand() % 3500;
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
	printf("Resultado de uma mochila com capacidade %d e %d variaveis, foi: %d\n", capacidade, n, mochila_limitantes(capacidade, pesos, variaveis, n));
	return 0;
}

