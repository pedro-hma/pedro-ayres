#include <stdio.h>
#include <string.h>

#define MAX_CONTAS 100

typedef struct{
    int numeroConta;
    char nomeCliente[100];
    char cpf[12];
    char telefone[15];
    float saldo;
} Conta;

int buscarConta(Conta contas[],int numContas,int numeroConta){
    if(numContas == 0){
        return -1;
    }
    for(int i = 0; i < numContas;i++){
        if(contas[i].numeroConta == numeroConta){
            return i;
        }
    }
    return -2;
}
void cadastrarConta(Conta contas[],int *numContas){
    if(*numContas >= MAX_CONTAS){
        printf("Limite de contas cadastradas atingido.\n");
        return;
    }
    int numeroconta;
    printf("Informe o número da nova conta: \n");
    scanf("%d",&numeroconta);

    if(buscarConta(contas,*numContas,numeroconta)>=0){
        printf("Numero de conta já cadastrado.\n");
        return;
    }
    contas[*numContas].numeroConta = numeroconta;
    printf("Informe o nome do cliente: ");
    scanf("%s", contas[*numContas].nomeCliente);
    printf("Informe o CPF do cliente: ");
    scanf("%s", contas[*numContas].cpf);
    printf("Informe o telefone do cliente: ");
    scanf("%s", contas[*numContas].telefone);
    contas[*numContas].saldo = 0.0;
    (*numContas)++;
    printf("Conta cadastrada com sucesso.\n");
}
void consultarSaldo(Conta contas [],int nConta,int numConta){
    int aux = buscarConta(contas,nConta,numConta);
    if(aux >= 0){
        printf("Saldo da conta %d: %.2f\n", numConta, contas[aux].saldo);
    } else if(aux == -1){
        printf("Cadastro de contas está vazio.\n");
    }else{
        printf("Conta não encontrada.\n");
    }
}
void fazerDeposito(Conta contas[], int numconta,int nconta){
    int aux = buscarConta(contas,numconta,nconta);
    if(aux >= 0){
       float valor;
        printf("Informe o valor do depósito: ");
        scanf("%f", &valor);
        contas[aux].saldo += valor;
        printf("Depósito realizado. Novo saldo: %.2f\n", contas[aux].saldo);
    } else if(aux == -1){
        printf("Cadastro de contas está vazio.\n");
    }else{
        printf("Conta não encontrada.\n");
    }    
}
void fazerSaque(Conta contas[], int conta,int conta1){
    int aux = buscarConta(contas,conta,conta1);
    if (aux >= 0) {
        float valor;
        printf("Informe o valor do saque: ");
        scanf("%f", &valor);
        if (contas[aux].saldo >= valor) {
            contas[aux].saldo -= valor;
            printf("Saque realizado. Novo saldo: %.2f\n", contas[aux].saldo);
        } else {
            printf("Saldo insuficiente.\n");
        }
    } else if (aux == -1) {
        printf("Cadastro de contas está vazio.\n");
    } else {
        printf("Conta não encontrada.\n");
    }
}
void exibirConta(Conta contas [], int contaS){
    for(int i = 0 ; i < contaS;i++){
        printf("Número da conta: %d, Nome do titular: %s, Telefone: %s\n", contas[i].numeroConta, contas[i].nomeCliente, contas[i].telefone);
    }
}

int main(){
    Conta contas [ MAX_CONTAS];
    int numContas = 0;
    int numConta = 0;
    int numconta = 0;
    int conta = 0;
    int contaS = 0;

    int aux = buscarConta(contas,numContas,12345);
    printf("Resultado da busca: %d\n ",aux);

    cadastrarConta(contas,&numContas);
    consultarSaldo(contas,numConta,contas[0].numeroConta);
    fazerDeposito(contas, numconta, contas[0].numeroConta);
    fazerSaque(contas, conta, contas[0].numeroConta);
    exibirConta(contas,contaS);

    return 0;
}