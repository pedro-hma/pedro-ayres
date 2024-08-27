import java.util.Scanner;

public class CalculadoraAvancada {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Escolha uma operação:");
            System.out.println("1. Adição (+)");
            System.out.println("2. Subtração (-)");
            System.out.println("3. Multiplicação (*)");
            System.out.println("4. Divisão (/)");
            System.out.println("5. Potenciação (^)");
            System.out.println("6. Raiz Quadrada (√)");
            System.out.println("7. Fatorial (!)");
            System.out.println("8. Sair");

            int opcao = scanner.nextInt();

            if (opcao == 8) {
                System.out.println("Saindo...");
                break;
            }

            double num1, num2, resultado;
            switch (opcao) {
                case 1: // Adição
                    System.out.print("Digite o primeiro número: ");
                    num1 = scanner.nextDouble();
                    System.out.print("Digite o segundo número: ");
                    num2 = scanner.nextDouble();
                    resultado = num1 + num2;
                    System.out.printf("Resultado: %.2f%n", resultado);
                    break;
                case 2: // Subtração
                    System.out.print("Digite o primeiro número: ");
                    num1 = scanner.nextDouble();
                    System.out.print("Digite o segundo número: ");
                    num2 = scanner.nextDouble();
                    resultado = num1 - num2;
                    System.out.printf("Resultado: %.2f%n", resultado);
                    break;
                case 3: // Multiplicação
                    System.out.print("Digite o primeiro número: ");
                    num1 = scanner.nextDouble();
                    System.out.print("Digite o segundo número: ");
                    num2 = scanner.nextDouble();
                    resultado = num1 * num2;
                    System.out.printf("Resultado: %.2f%n", resultado);
                    break;
                case 4: // Divisão
                    System.out.print("Digite o primeiro número: ");
                    num1 = scanner.nextDouble();
                    System.out.print("Digite o segundo número: ");
                    num2 = scanner.nextDouble();
                    if (num2 != 0) {
                        resultado = num1 / num2;
                        System.out.printf("Resultado: %.2f%n", resultado);
                    } else {
                        System.out.println("Erro: Divisão por zero.");
                    }
                    break;
                case 5: // Potenciação
                    System.out.print("Digite a base: ");
                    num1 = scanner.nextDouble();
                    System.out.print("Digite o expoente: ");
                    num2 = scanner.nextDouble();
                    resultado = Math.pow(num1, num2);
                    System.out.printf("Resultado: %.2f%n", resultado);
                    break;
                case 6: // Raiz Quadrada
                    System.out.print("Digite o número: ");
                    num1 = scanner.nextDouble();
                    if (num1 >= 0) {
                        resultado = Math.sqrt(num1);
                        System.out.printf("Resultado: %.2f%n", resultado);
                    } else {
                        System.out.println("Erro: Não é possível calcular a raiz quadrada de um número negativo.");
                    }
                    break;
                case 7: // Fatorial
                    System.out.print("Digite um número inteiro não negativo: ");
                    int num = scanner.nextInt();
                    if (num < 0) {
                        System.out.println("Erro: O número deve ser não negativo.");
                    } else {
                        System.out.printf("Resultado: %d%n", fatorial(num));
                    }
                    break;
                default:
                    System.out.println("Opção inválida.");
                    break;
            }
        }
        scanner.close();
    }

    private static int fatorial(int n) {
        int resultado = 1;
        for (int i = 1; i <= n; i++) {
            resultado *= i;
        }
        return resultado;
    }
}