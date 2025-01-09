import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Tente adivinhar o número que estou pensando entre 1 e 100.")

    tentativas = 0
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, insira um número válido.")

# Inicie o jogo chamando a função
jogo_adivinhacao()
