#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NOME 50
#define MAX_DESCRICAO 100
#define MAX_CATEGORIA 50
#define MAX_VIDEOS 20

typedef struct {
    int id;
    char titulo[MAX_NOME];
    char descricao[MAX_DESCRICAO];
    char categoria[MAX_CATEGORIA];
    int duracao;
} VIDEO;

typedef struct {
    int id;
    char nome[MAX_NOME];
    int favoritos;
    int videosfavoritos[MAX_VIDEOS];
} CADASTROUSUARIO;

void salvar_arquivo(const char *filename, void *data, size_t size) {
    FILE *arquivo = fopen(filename, "ab");
    if (!arquivo) {
        printf("Erro ao abrir o arquivo.");
        return;
    }
    fwrite(data, size, 1, arquivo);
    fclose(arquivo);
}
void listar_arquivo(const char *filename, size_t size, void (*print_func)(void *)) {
    FILE *arquivo = fopen(filename, "rb");
    if (!arquivo) {
        printf("Erro ao abrir o arquivo.");
        return;
    }
    void *data = malloc(size);
    while (fread(data, size, 1, arquivo)) {
        print_func(data);
    }
    free(data);
    fclose(arquivo);
}
void exibir_video(void *data) {
    VIDEO *video = (VIDEO *)data;
    printf("ID: %d\nTítulo: %s\nDescrição: %s\nCategoria: %s\nDuração: %d minutos\n\n",
           video->id, video->titulo, video->descricao, video->categoria, video->duracao);
}
void exibir_usuario(void *data) {
    CADASTROUSUARIO *usuario = (CADASTROUSUARIO *)data;
    printf("ID: %d\nNome: %s\nNúmero de Favoritos: %d\nVídeos Favoritos: ", 
           usuario->id, usuario->nome, usuario->favoritos);
    for (int i = 0; i < usuario->favoritos; i++) {
        printf("%d ", usuario->videosfavoritos[i]);
    }
    printf("\n\n");
}
void cadastrar_usuario(){
    FILE *arquivo = fopen("usuarios.bin","ab");
    if (!arquivo) {
        printf("Erro ao abrir o arquivo.");
        return;
    }
    CADASTROUSUARIO usuario;

    printf("\nCadastro do usuario\n ");
    printf("ID do usuario: ");
    scanf("%d",&usuario.id);
    printf("Nome do usuario: ");
    scanf(" %[^\n]", usuario.nome);
    printf("Numero de videos favoritos: ");
    scanf("%d",&usuario.favoritos);

    for(int i = 0; i < usuario.favoritos; i++){
        printf("ID do(s) video(s) favorito(s) %d",i +1);
        scanf("%d",&usuario.videosfavoritos);
    }
    fwrite(&usuario,sizeof(CADASTROUSUARIO),1,arquivo);
    fclose(arquivo);

    printf("Usuario Cadstrado com sucesso.");
}
void listar_usuario(){
    FILE *arquivo = fopen("usuarios.bin","rb");
    if(!arquivo){
        printf("Erro ao abrir o arquivo de usuarios");
        return;
    }
    CADASTROUSUARIO usuario;
    printf("\ Lista de Usuario\n");
    while(fread(&usuario,sizeof(CADASTROUSUARIO),1,arquivo)){
        printf("ID do usuario: %d\n",usuario.id);
        printf("Nome do usuario :  %d\n",usuario.nome);
        printf("Numero de video(s) favoritos:  %d\n",usuario.favoritos);

        for(int i = 0; i < usuario.favoritos; i++){
        printf("%d",usuario.videosfavoritos);
        }
        printf("\n \n");
    }
    fclose(arquivo);
}
void remover_usuario(int id){
    FILE *arquivo = fopen("usuarios.bin","rb");
    FILE *arquivo_temporario = fopen("usuarios_temporarios.bin","wb");
    if (!arquivo) {
        printf("Erro ao abrir o arquivo.");
        return;
    }
    CADASTROUSUARIO usuario;
    int encontrado = 0;

    while(fread(&usuario,sizeof(CADASTROUSUARIO),1,arquivo)){
        if(usuario.id != id){
            fread(&usuario,sizeof(CADASTROUSUARIO),1,arquivo_temporario);
        } else{
            encontrado = 1;
            printf("Usuario com id %d foi removido",id);
        }
    }
    fclose(arquivo);
    fclose(arquivo_temporario);

    remove("usuarios.bin");
    remove("usuarios temporarios.bin");

    if(!encontrado){
        printf("Usuario com id %d não encontado",id);
    }
}
void cadastrar_video(){
    FILE *arquivo = fopen("videos.bin","ab");
    if(!arquivo){
        printf("Erro ao abrir o arquivo de videos");
        return;
    }
    VIDEO video;
    printf("ID do video: ");
    scanf("%d",&video.id);
    printf("Titulo do video: ");
   scanf(" %[^\n]", video.titulo);
    printf("Descrição do video: ");
    scanf(" %[^\n]", video.descricao);
    printf("Categoria do video: ");
    scanf(" %[^\n]", video.categoria);
    printf("Duração do video em minutos: ");
    scanf("%d",&video.duracao);

    fwrite(&video,sizeof(VIDEO),1,arquivo);
    fclose(arquivo);

    printf("Video cadastrado com sucesso\n");
}
void listar_video(){
    FILE *arquivo = fopen("videos.bin","rb");
    if(!arquivo){
        printf("Erro ao abrir o arquivo de video");
        return;
    }
    VIDEO video;
    printf("\ Lista Videos\n");
    while(fread(&video,sizeof(VIDEO),1,arquivo)){
        printf("ID : %d\n",video.id);
        printf("Titulo do video :  %d\n",video.titulo);
        printf("Categoria do video:  %d\n",video.categoria);
        printf("Tempo de duração do video : %d\n",video.duracao);
        printf("Descrição do video: %d\n",video.descricao);
    }
}
int main() {
    int opcao, id;
    while (1) {
        printf("\nMenu:\n");
        printf("1. Cadastrar vídeo\n");
        printf("2. Cadastrar usuário\n");
        printf("3. Listar vídeos\n");
        printf("4. Listar usuários\n");
        printf("5. Remover usuário\n");
        printf("6. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                cadastrar_video();
                break;
            case 2:
                cadastrar_usuario();
                break;
            case 3:
                listar_arquivo("videos.bin", sizeof(VIDEO), exibir_video);
                break;
            case 4:
                listar_arquivo("usuarios.bin", sizeof(CADASTROUSUARIO), exibir_usuario);
                break;
            case 5:
                printf("ID do usuário para remover: ");
                scanf("%d", &id);
                remover_usuario(id);
                break;
            case 6:
                printf("Saindo do programa.\n");
                return 0;
            default:
                printf("Opção inválida!\n");
        }
    }
    return 0;
}