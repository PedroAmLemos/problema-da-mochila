// A Dynamic Programming based
// solution for 0-1 Knapsack problem
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
int knapSack(int W, int wt[], int val[], int n)
{
	int i, w;
	int K[n + 1][W + 1];

	// Build table K[][] in bottom up manner
	for (i = 0; i <= n; i++)
	{
		for (w = 0; w <= W; w++)
		{
			if (i == 0 || w == 0)
				K[i][w] = 0;
			else if (wt[i - 1] <= w)
				K[i][w] = max(val[i - 1]
						+ K[i - 1][w - wt[i - 1]],
						K[i - 1][w]);
			else
				K[i][w] = K[i - 1][w];
		}
	}

	return K[n][W];
}

int soma(int vetor[]){
	int i = 0;
	for(int k = 0; k < sizeof(*vetor); k++){
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
	int val[1000];
	int wt[1000];
	for (int i = 0; i < 1000; i++) {
		random_number = rand() % 10000;
		val[i] = random_number;
		random_number = rand() % 10000;
		wt[i] = random_number;
	}
	int W;
	int resSoma = soma(wt);
	if(resSoma/2 < maior(wt)){
		W = resSoma/2 + maior(wt);
	}else{
		W = resSoma/2;
	}
	int n = sizeof(val) / sizeof(val[0]);
	printf("%d", knapSack(W, wt, val, n));
	return 0;
}

