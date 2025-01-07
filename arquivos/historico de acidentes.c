# include <stdio.h>

# define NUM_ESTADOS 26
 struct Estados {
    char nome[50];
    int numVeiculos;
    int numAcidentes;
};

void dados(struct Estados estados[]);
void contarAcidentes(struct Estados estados[], int *maxAcidentes, int *minAcidentes);
float percentualAcidentes(struct Estados estado);
float mediaAcidentes(struct Estados estados[]);
void estadosAcimaMedia(struct Estados estados[], float media);

void dados (struct Estados estados []){
        for (int i = 0; i < NUM_ESTADOS;i++){
            printf("Informe o nome do seu estados: ");
            scanf("%s",estados[i].nome);
            printf("Informe o numero de veiculos do seu estados: ");
            scanf("%d",&estados[i].numVeiculos);
            printf("Informe o numero de acidentes do seu estados: ");
            scanf("%d",&estados[i].numAcidentes);
        }
}
void contarAcidentes(struct Estados estados[],int *maxAcidentes,int *minAcidentes){
    *maxAcidentes = 0;
    *minAcidentes = 0;
    for(int i = 1; i < NUM_ESTADOS; i++){
        if(estados[i].numAcidentes > estados[*maxAcidentes].numAcidentes){
             *maxAcidentes = i;
                }
            if(estados[i].numAcidentes > estados[*maxAcidentes].numAcidentes){
             *minAcidentes = i;
        }
    }
}
float percentualAcidentes (struct Estados estados){
    return ((float)estados.numAcidentes/estados.numVeiculos);
}
float mediaAcidentes(struct Estados estados[]) {
    int soma = 0;
    for (int i = 0; i < NUM_ESTADOS; i++) {
        soma += estados[i].numAcidentes;
    }
    return (float)soma / NUM_ESTADOS;
}

void estadosAcimaMedia(struct Estados estados[], float media) {
    printf("Estados acima da média de acidentes:\n");
    for (int i = 0; i < NUM_ESTADOS; i++) {
        if (estados[i].numAcidentes > media) {
            printf("%s\n", estados[i].nome);
        }
    }
}

int main() {
    struct Estados estados[NUM_ESTADOS];
    dados(estados);
    
    int maxAcidentes, minAcidentes;
    contarAcidentes(estados, &maxAcidentes, &minAcidentes);
    
    float media = mediaAcidentes(estados);
    estadosAcimaMedia(estados, media);

    for (int i = 0; i < NUM_ESTADOS; i++) {
        printf("Percentual de acidentes no estado %s: %.2f%%\n", estados[i].nome, percentualAcidentes(estados[i]));
    }

    printf("Estado com mais acidentes: %s com %d acidentes\n", estados[maxAcidentes].nome, estados[maxAcidentes].numAcidentes);
    printf("Estado com menos acidentes: %s com %d acidentes\n", estados[minAcidentes].nome, estados[minAcidentes].numAcidentes);
    printf("Média de acidentes no país: %.2f\n", media);

    return 0;
}