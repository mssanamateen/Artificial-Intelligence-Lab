import tensorflow as tf
import numpy as np
import random
class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.players = ["X", "O"]
        self.current_player = None
        self.winner = None
        self.game_over = False

    def reset(self):
        self.board = np.zeros((3, 3))
        self.current_player = None
        self.winner = None
        self.game_over = False

    def available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    moves.append((i, j))
        return moves

    def make_move(self, move):
        if self.board[move[0]][move[1]] != 0:
            return False
        self.board[move[0]][move[1]] = self.players.index(self.current_player) + 1
        self.check_winner()
        self.switch_player()
        return True

    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def check_winner(self):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                self.winner = self.players[int(self.board[i][0] - 1)]
                self.game_over = True
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != 0:
                self.winner = self.players[int(self.board[0][j] - 1)]
                self.game_over = True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.winner = self.players[int(self.board[0][0] - 1)]
            self.game_over = True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.winner = self.players[int(self.board[0][2] - 1)]
            self.game_over = True

    def print_board(self):
        print("-------------")
        for i in range(3):
            print("|", end=" ")
            for j in range(3):
                print(self.players[int(self.board[i][j] - 1)] if self.board[i][j] != 0 else " ", end="|")
            print()
            print("-------------")


game = TicTacToe()
game.current_player = game.players[0]
game.print_board()

while not game.game_over:
    move = input(f"{game.current_player}''s turn. Enter row and column (e.g. 0 0): ")
    move = tuple(map(int, move.split()))
    while move not in game.available_moves():
        move = input("Invalid move. Try again: ")
        move = tuple(map(int, move.split()))
    game.make_move(move)
    game.print_board()

if game.winner:
    print(f"{game.winner} wins!")
else:
    print("It''s a tie!")
