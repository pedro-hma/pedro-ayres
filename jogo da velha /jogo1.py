import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.current_player = "X"
        self.board = [ [None for _ in range(3)] for _ in range(3) ]
        self.buttons = [ [None for _ in range(3)] for _ in range(3) ]
        self.create_board()
        
    def create_board(self):
        for row in range(3):
            for col in range(3):
                # Cria um botão para cada célula do tabuleiro
                button = tk.Button(self.root, text="", font=('Arial', 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.board[row][col] is None:
            # Atualiza o estado do tabuleiro
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner(self.current_player):
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.current_player} venceu!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reset_board()
            else:
                # Alterna o jogador
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        # Verifica linhas
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Verifica colunas
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        # Verifica diagonais
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(all(cell is not None for cell in row) for row in self.board)

    def reset_board(self):
        self.current_player = "X"
        self.board = [ [None for _ in range(3)] for _ in range(3) ]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
