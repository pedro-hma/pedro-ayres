#include <stdio.h>
#include <string.h>

int main() {
    int N;
    scanf("%d\n", &N);

    for (int i = 0; i < N; i++) {
        char line[101];
        fgets(line, sizeof(line), stdin);

        char hidden_message[101];
        int index = 0;
        int in_word = 0;

        for (int j = 0; line[j] != '\0'; j++) {
            if (line[j] != ' ' && line[j] != '\n') {
                if (!in_word) {
                    hidden_message[index++] = line[j];
                    in_word = 1;
                }
            } else {
                in_word = 0;
            }
        }

        hidden_message[index] = '\0';
        printf("%s\n", hidden_message);
    }

    return 0;
}