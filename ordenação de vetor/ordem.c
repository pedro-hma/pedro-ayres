#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void geraVetor(int *vetor, int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        vetor[i] = rand() % 1000000; // Números aleatórios até 1 milhão
    }
}
void preencheVetorOrdenado(int *vetor, int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        vetor[i] = i;
    }
}
void preencheVetorOrdenadoDecrescente(int *vetor, int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        vetor[i] = tamanho - i - 1;
    }
}
void bubbleSort(int *vetor, int tamanho) {
    for (int i = 0; i < tamanho - 1; i++) {
        for (int j = 0; j < tamanho - 1 - i; j++) {
            if (vetor[j] > vetor[j + 1]) {
                int temp = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = temp;
            }
        }
    }
}
void insertionSort(int *vetor, int tamanho) {
    for (int i = 1; i < tamanho; i++) {
        int key = vetor[i];
        int j = i - 1;
        while (j >= 0 && vetor[j] > key) {
            vetor[j + 1] = vetor[j];
            j--;
        }
        vetor[j + 1] = key;
    }
}
void selectionSort(int *vetor, int tamanho) {
    for (int i = 0; i < tamanho - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < tamanho; j++) {
            if (vetor[j] < vetor[minIdx]) {
                minIdx = j;
            }
        }
        if (minIdx != i) {
            int temp = vetor[i];
            vetor[i] = vetor[minIdx];
            vetor[minIdx] = temp;
        }
    }
}
double medeTempo(void (*funcaoOrdenacao)(int *, int), int *vetor, int tamanho) {
    clock_t inicio = clock();
    funcaoOrdenacao(vetor, tamanho);
    clock_t fim = clock();
    return ((double)(fim - inicio)) / CLOCKS_PER_SEC * 1000; 
}
int main() {
    int tamanhos[] = {10, 100, 1000, 10000, 100000, 1000000, 10000000};
    int numTamanhos = sizeof(tamanhos) / sizeof(tamanhos[0]);
    double temposBubbleSort[3][7], temposInsertionSort[3][7], temposSelectionSort[3][7];
    for (int t = 0; t < numTamanhos; t++) {
        int tamanho = tamanhos[t];
        int *vetorDesordenado = (int *)malloc(tamanho * sizeof(int));
        int *vetorOrdenado = (int *)malloc(tamanho * sizeof(int));
        int *vetorDecrescente = (int *)malloc(tamanho * sizeof(int));

        geraVetor(vetorDesordenado, tamanho);
        preencheVetorOrdenado(vetorOrdenado, tamanho);
        preencheVetorOrdenadoDecrescente(vetorDecrescente, tamanho);

        temposBubbleSort[0][t] = medeTempo(bubbleSort, vetorDesordenado, tamanho);
        temposBubbleSort[1][t] = medeTempo(bubbleSort, vetorOrdenado, tamanho);
        temposBubbleSort[2][t] = medeTempo(bubbleSort, vetorDecrescente, tamanho);

        temposInsertionSort[0][t] = medeTempo(insertionSort, vetorDesordenado, tamanho);
        temposInsertionSort[1][t] = medeTempo(insertionSort, vetorOrdenado, tamanho);
        temposInsertionSort[2][t] = medeTempo(insertionSort, vetorDecrescente, tamanho);

        temposSelectionSort[0][t] = medeTempo(selectionSort, vetorDesordenado, tamanho);
        temposSelectionSort[1][t] = medeTempo(selectionSort, vetorOrdenado, tamanho);
        temposSelectionSort[2][t] = medeTempo(selectionSort, vetorDecrescente, tamanho);
        if (temposBubbleSort[0][t] > 300000 || temposInsertionSort[0][t] > 300000 || temposSelectionSort[0][t] > 300000) {
            if (t > 0) {
                t--;
                break;
            }
        }
        free(vetorDesordenado);
        free(vetorOrdenado);
        free(vetorDecrescente);
    }
    printf("Tempos BubbleSort:\n");
    for (int i = 0; i < numTamanhos; i++) {
        printf("Tamanho %d: %.3f ms (Desordenado), %.3f ms (Ordenado), %.3f ms (Decrescente)\n",
               tamanhos[i], temposBubbleSort[0][i], temposBubbleSort[1][i], temposBubbleSort[2][i]);
    }
    printf("\nTempos InsertionSort:\n");
    for (int i = 0; i < numTamanhos; i++) {
        printf("Tamanho %d: %.3f ms (Desordenado), %.3f ms (Ordenado), %.3f ms (Decrescente)\n",
               tamanhos[i], temposInsertionSort[0][i], temposInsertionSort[1][i], temposInsertionSort[2][i]);
    }
    printf("\nTempos SelectionSort:\n");
    for (int i = 0; i < numTamanhos; i++) {
        printf("Tamanho %d: %.3f ms (Desordenado), %.3f ms (Ordenado), %.3f ms (Decrescente)\n",
               tamanhos[i], temposSelectionSort[0][i], temposSelectionSort[1][i], temposSelectionSort[2][i]);
    }
    return 0;
}