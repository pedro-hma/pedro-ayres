import random

# Classe Personagem
class Personagem:
    def __init__(self, nome, hp, ataque, defesa):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa + random.randint(-2, 2))  # Dano com pequena variação aleatória
        alvo.hp -= dano
        return dano

# Função principal do combate
def combate(jogador, inimigo):
    rodada = 1
    while jogador.hp > 0 and inimigo.hp > 0:
        print(f"\n--- Rodada {rodada} ---")
        print(f"{jogador.nome}: {jogador.hp} HP")
        print(f"{inimigo.nome}: {inimigo.hp} HP")

        # Escolha do jogador
        print("\nEscolha sua ação:")
        print("1. Atacar")
        print("2. Defender")
        acao = input("Digite o número da sua ação: ")

        if acao == "1":
            dano_causado = jogador.atacar(inimigo)
            print(f"{jogador.nome} atacou {inimigo.nome} e causou {dano_causado} de dano!")
        elif acao == "2":
            defesa_temporaria = jogador.defesa + random.randint(1, 3)
            print(f"{jogador.nome} se defendeu e aumentou sua defesa para {defesa_temporaria} nesta rodada!")
        else:
            print("Ação inválida! Você perdeu sua vez.")
            defesa_temporaria = jogador.defesa

        # Verifica se o inimigo foi derrotado
        if inimigo.hp <= 0:
            print(f"{inimigo.nome} foi derrotado! {jogador.nome} venceu!")
            break

        # Inimigo ataca jogador
        dano_recebido = max(0, inimigo.atacar(jogador) if acao != "2" else inimigo.ataque - defesa_temporaria + random.randint(-2, 2))
        jogador.hp -= dano_recebido
        print(f"{inimigo.nome} atacou {jogador.nome} e causou {dano_recebido} de dano!")

        # Verifica se o jogador foi derrotado
        if jogador.hp <= 0:
            print(f"{jogador.nome} foi derrotado! {inimigo.nome} venceu!")
            break

        rodada += 1

# Exemplo de uso
if __name__ == "__main__":
    # Criar jogador e inimigo
    jogador = Personagem(nome="Herói", hp=50, ataque=10, defesa=5)
    inimigo = Personagem(nome="Goblin", hp=30, ataque=8, defesa=3)

    # Iniciar combate
    combate(jogador, inimigo)
