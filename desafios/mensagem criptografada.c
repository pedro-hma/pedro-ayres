#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    int C;
    scanf("%d", &C);

    char mensagem[101];

    for (int i = 0; i < C; i++) {
        scanf("%s", mensagem);

        int tamanho = strlen(mensagem);
        for (int j = tamanho - 1; j >= 0; j--) {
            if (islower(mensagem[j])) {
                printf("%c", mensagem[j]);
            }
        }
        printf("\n");
    }

    return 0;
}