import os
os.environ["SDL_AUDIODRIVER"] = "dummy"  # Desabilita o áudio

import pygame
import random
import sys

# Definições de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)  # Cor para o jogador em movimento

# Configurações do labirinto
CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 20

# Direções para movimentação
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[1 for _ in range(width)] for _ in range(height)]
        self.start = (0, 0)
        self.end = (width - 1, height - 1)

    def generate(self):
        def dfs(x, y):
            self.grid[y][x] = 0
            random.shuffle(DIRECTIONS)
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx] == 1:
                    if self._count_adjacent_open_cells(nx, ny) <= 1:
                        dfs(nx, ny)

        dfs(*self.start)
        self.grid[self.end[1]][self.end[0]] = 0

    def _count_adjacent_open_cells(self, x, y):
        count = 0
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                count += self.grid[ny][nx] == 0
        return count

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
        pygame.display.set_caption("Labirinto")
        self.clock = pygame.time.Clock()

        self.maze = Maze(GRID_WIDTH, GRID_HEIGHT)
        self.maze.generate()

        self.player_pos = list(self.maze.start)

    def draw_grid(self):
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                color = WHITE if self.maze.grid[y][x] == 0 else BLACK
                pygame.draw.rect(self.screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Desenhar início e fim
        pygame.draw.rect(self.screen, GREEN, (self.maze.start[0] * CELL_SIZE, self.maze.start[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, RED, (self.maze.end[0] * CELL_SIZE, self.maze.end[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Desenhar jogador
        pygame.draw.rect(self.screen, BLUE, (self.player_pos[0] * CELL_SIZE, self.player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def move_player(self, dx, dy):
        new_x, new_y = self.player_pos[0] + dx, self.player_pos[1] + dy
        if 0 <= new_x < self.maze.width and 0 <= new_y < self.maze.height and self.maze.grid[new_y][new_x] == 0:
            self.player_pos = [new_x, new_y]
            print(f"Jogador se moveu para {self.player_pos}")  # Log do movimento

    def run(self):
        print("Iniciando o jogo...")
        running = True
        while running:
            keys = pygame.key.get_pressed()  # Captura teclas pressionadas diretamente
            if keys[pygame.K_UP]:
                self.move_player(0, -1)
            if keys[pygame.K_DOWN]:
                self.move_player(0, 1)
            if keys[pygame.K_LEFT]:
                self.move_player(-1, 0)
            if keys[pygame.K_RIGHT]:
                self.move_player(1, 0)

            for event in pygame.event.get():
                print(event)  # Log de eventos para depuração
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(BLACK)
            self.draw_grid()
            pygame.display.flip()
            self.clock.tick(10)  # Reduziu FPS para facilitar depuração

            if tuple(self.player_pos) == self.maze.end:
                print("Você venceu!")
                running = False

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    print("Inicializando o Labirinto...")
    game = Game()
    game.run()
