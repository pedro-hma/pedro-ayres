import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 600, 600
TAMANHO_CELULA = LARGURA // 3
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Velha")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Fonte
FONTE = pygame.font.Font(None, 80)

# Inicializa o tabuleiro
tabuleiro = [""] * 9
turno = "X"

# Desenha as linhas do tabuleiro
def desenhar_linhas():
    for i in range(1, 3):
        pygame.draw.line(TELA, PRETO, (0, TAMANHO_CELULA * i), (LARGURA, TAMANHO_CELULA * i), 5)
        pygame.draw.line(TELA, PRETO, (TAMANHO_CELULA * i, 0), (TAMANHO_CELULA * i, ALTURA), 5)

# Desenha os símbolos no tabuleiro
def desenhar_simbolos():
    for i in range(9):
        x = (i % 3) * TAMANHO_CELULA + TAMANHO_CELULA // 2
        y = (i // 3) * TAMANHO_CELULA + TAMANHO_CELULA // 2
        if tabuleiro[i] == "X":
            texto = FONTE.render("X", True, VERMELHO)
            TELA.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))
        elif tabuleiro[i] == "O":
            texto = FONTE.render("O", True, PRETO)
            TELA.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))

# Verifica se há um vencedor
def verificar_vencedor():
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combinacao in combinacoes:
        a, b, c = combinacao
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] != "":
            return tabuleiro[a]
    if "" not in tabuleiro:
        return "Empate"
    return None

# Reinicia o jogo
def reiniciar_jogo():
    global tabuleiro, turno
    tabuleiro = [""] * 9
    turno = "X"

# Loop principal
def main():
    global turno
    rodando = True
    while rodando:
        TELA.fill(BRANCO)
        desenhar_linhas()
        desenhar_simbolos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pygame.mouse.get_pos()
                linha = y // TAMANHO_CELULA
                coluna = x // TAMANHO_CELULA
                idx = linha * 3 + coluna
                if tabuleiro[idx] == "":
                    tabuleiro[idx] = turno
                    vencedor = verificar_vencedor()
                    if vencedor:
                        if vencedor == "Empate":
                            print("Empate!")
                        else:
                            print(f"O jogador {vencedor} venceu!")
                        reiniciar_jogo()
                    else:
                        turno = "O" if turno == "X" else "X"

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
