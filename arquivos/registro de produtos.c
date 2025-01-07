# include <stdio.h>
# include <string.h>

# define MAX_PRODUTOS 40

typedef struct  {
    int codigo;
    char descricao[100];
    float valorUnitario;
    int quantidadeEstoque;
}Produto;
void cadastrarProduto(Produto produtos[],int *numProdutos){
    if(*numProdutos >= MAX_PRODUTOS){
        printf("Limite de produtos cadastrados atingido.\n");
        return;
    }
    printf("Informe o código do produto: ");
    scanf("%d", &produtos[*numProdutos].codigo);
    printf("Informe a descrição do produto: ");
    scanf("%s", produtos[*numProdutos].descricao);
    printf("Informe o valor unitário do produto: ");
    scanf("%f", &produtos[*numProdutos].valorUnitario);
    printf("Informe a quantidade em estoque: ");
    scanf("%d", &produtos[*numProdutos].quantidadeEstoque);
    (*numProdutos)++;
}
void alterarValorUnitario(Produto produtos[], int numProdutos, int codigo) {
    for (int i = 0; i < numProdutos; i++) {
        if (produtos[i].codigo == codigo) {
            printf("Informe o novo valor unitário do produto %s: ", produtos[i].descricao);
            scanf("%f", &produtos[i].valorUnitario);
            printf("Valor unitário atualizado com sucesso.\n");
            return;
        }
    }
    printf("Produto com código %d não encontrado.\n", codigo);
}
float informarValorUnitario(Produto produtos[], int numProdutos, int codigo) {
    for (int i = 0; i < numProdutos; i++) {
        if (produtos[i].codigo == codigo) {
            return produtos[i].valorUnitario;
        }
    }
    return -1;
}
int informarQuantidadeEstoque(Produto produtos[], int numProdutos, int codigo) {
    for (int i = 0; i < numProdutos; i++) {
        if (produtos[i].codigo == codigo) {
            return produtos[i].quantidadeEstoque;
        }
    }
    return -1;
}
void venderProduto(Produto produtos[], int numProdutos, int codigo, int quantidadeDesejada) {
    for (int i = 0; i < numProdutos; i++) {
        if (produtos[i].codigo == codigo) {
            if (produtos[i].quantidadeEstoque == 0) {
                printf("Produto %s está com estoque zero.\n", produtos[i].descricao);
                return;
            } else if (produtos[i].quantidadeEstoque < quantidadeDesejada) {
                printf("Quantidade desejada menor que a quantidade em estoque. Deseja efetivar a compra? (1-Sim, 0-Não): ");
                int opcao;
                scanf("%d", &opcao);
                if (opcao == 1) {
                    printf("Compra realizada. Valor total: %.2f\n", produtos[i].quantidadeEstoque * produtos[i].valorUnitario);
                    produtos[i].quantidadeEstoque = 0;
                } else {
                    printf("Compra não realizada.\n");
                }
            } else {
                produtos[i].quantidadeEstoque -= quantidadeDesejada;
                printf("Compra realizada. Valor total: %.2f\n", quantidadeDesejada * produtos[i].valorUnitario);
            }
            return;
        }
    }
    printf("Produto com código %d não encontrado.\n", codigo);
}
void atualizarQuantidadeEstoque(Produto produtos[], int numProdutos, int codigo, int novaQuantidade) {
    for (int i = 0; i < numProdutos; i++) {
        if (produtos[i].codigo == codigo) {
            produtos[i].quantidadeEstoque = novaQuantidade;
            printf("Quantidade em estoque do produto %s atualizada para %d.\n", produtos[i].descricao, novaQuantidade);
            return;
        }
    }
    printf("Produto com código %d não encontrado.\n", codigo);
}
void exibirTodosProdutos(Produto produtos[], int numProdutos) {
    for (int i = 0; i < numProdutos; i++) {
        printf("Código: %d, Descrição: %s\n", produtos[i].codigo, produtos[i].descricao);
    }
}
void exibirProdutosEstoqueZero(Produto produtos[], int numProdutos) {
    printf("Produtos com estoque zero:\n");
    for (int i = 0; i < numProdutos; i++) {
        if (produtos[i].quantidadeEstoque == 0) {
            printf("Código: %d, Descrição: %s\n", produtos[i].codigo, produtos[i].descricao);
        }
    }
}

int main(){
    Produto produtos [MAX_PRODUTOS];
    int numProdutos = 0;
    cadastrar(produtos,&numProdutos);
    alterarValorUnitario(produtos, numProdutos, produtos[0].codigo);
    float valor = informarValorUnitario(produtos, numProdutos, produtos[0].codigo); // Exemplo para o primeiro produto
    if (valor != -1) {
        printf("O valor unitário do produto é: %.2f\n", valor);
    } else {
        printf("Produto não encontrado.\n");
    }
    int quantidade = informarQuantidadeEstoque(produtos, numProdutos, produtos[0].codigo); // Exemplo para o primeiro produto
    if (quantidade != -1) {
        printf("A quantidade em estoque do produto é: %d\n", quantidade);
    } else {
        printf("Produto não encontrado.\n");
    }
     venderProduto(produtos, numProdutos, produtos[0].codigo, 5);
     atualizarQuantidadeEstoque(produtos, numProdutos, produtos[0].codigo, 100);
     exibirTodosProdutos(produtos, numProdutos);
     exibirProdutosEstoqueZero(produtos, numProdutos);

    return 0;
}