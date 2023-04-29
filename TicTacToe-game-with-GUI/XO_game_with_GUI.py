import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [[" ", " ", " "] for _ in range(3)]
        self.create_board()

    def create_board(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text=" ", font=("Arial", 30), width=2, height=1,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.update_button_text(row, col)
            if self.check_win(self.current_player):
                self.show_message_box(f"{self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                self.show_message_box("Tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def update_button_text(self, row, col):
        button = self.window.grid_slaves(row=row, column=col)[0]
        button.config(text=self.current_player)

    def is_board_full(self):
        return all([spot != " " for row in self.board for spot in row])

    def check_win(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def reset_board(self):
        self.board = [[" ", " ", " "] for _ in range(3)]
        for button in self.window.grid_slaves():
            button.config(text=" ")
        self.current_player = "X"

    def show_message_box(self, message):
        messagebox.showinfo("Game Over", message)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
