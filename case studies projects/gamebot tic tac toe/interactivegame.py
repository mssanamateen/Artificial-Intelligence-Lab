import numpy as np
import random

# TicTacToe Class
class TicTacToe:
    def __init__(self, state=None):
        self.board = np.zeros((3, 3)) if state is None else np.array(state)
        self.players = ["X", "O"]
        self.current_player = self.players[0]
        self.winner = None
        self.game_over = False

    def make_move(self, move):
        if self.board[move[0]][move[1]] != 0:
            return self.board, -10, self.game_over  # Invalid move penalty
        self.board[move[0]][move[1]] = self.players.index(self.current_player) + 1
        self.check_winner()
        reward = 1 if self.winner else 0
        self.switch_player()
        return self.board, reward, self.game_over

    def reset(self):
        self.board = np.zeros((3, 3))
        self.current_player = self.players[0]
        self.winner = None
        self.game_over = False

    def available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]

    def switch_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                self.winner = self.players[int(self.board[i][0] - 1)]
                self.game_over = True
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != 0:
                self.winner = self.players[int(self.board[0][j] - 1)]
                self.game_over = True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.winner = self.players[int(self.board[0][0] - 1)]
            self.game_over = True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.winner = self.players[int(self.board[0][2] - 1)]
            self.game_over = True
        if not any(0 in row for row in self.board):
            self.game_over = True

    def print_board(self):
        print("-------------")
        for i in range(3):
            print("|", end=" ")
            for j in range(3):
                print(self.players[int(self.board[i][j] - 1)] if self.board[i][j] != 0 else " ", end=" | ")
            print("\n-------------")

# Q-Learning Agent
class QLearningAgent:
    def __init__(self, alpha, epsilon, discount_factor):
        self.Q = {}
        self.alpha = alpha
        self.epsilon = epsilon
        self.discount_factor = discount_factor

    def get_Q_value(self, state, action):
        if (tuple(state.flatten()), action) not in self.Q:
            self.Q[(tuple(state.flatten()), action)] = 0.0
        return self.Q[(tuple(state.flatten()), action)]

    def choose_action(self, state, available_moves):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(available_moves)
        else:
            Q_values = [self.get_Q_value(state, action) for action in available_moves]
            max_Q = max(Q_values)
            best_moves = [action for action, Q_value in zip(available_moves, Q_values) if Q_value == max_Q]
            return random.choice(best_moves)

    def update_Q_value(self, state, action, reward, next_state, next_available_moves):
        current_Q = self.get_Q_value(state, action)
        if next_available_moves:
            next_Q = max([self.get_Q_value(next_state, next_action) for next_action in next_available_moves])
        else:
            next_Q = 0
        self.Q[(tuple(state.flatten()), action)] = current_Q + self.alpha * (reward + self.discount_factor * next_Q - current_Q)

# Train the Q-learning Agent
def train(num_episodes, alpha, epsilon, discount_factor):
    agent = QLearningAgent(alpha, epsilon, discount_factor)
    for _ in range(num_episodes):
        game = TicTacToe()
        state = game.board
        while not game.game_over:
            available_moves = game.available_moves()
            action = agent.choose_action(state, available_moves)
            next_state, reward, game_over = game.make_move(action)
            agent.update_Q_value(state, action, reward, next_state, game.available_moves())
            state = next_state
    return agent

# Play with the Agent
def play_with_agent(agent):
    game = TicTacToe()
    print("Let's play Tic Tac Toe!")
    print("You are 'O'. The agent is 'X'.")
    game.print_board()

    while not game.game_over:
        if game.current_player == "O":  # Your turn
            try:
                move = input("Enter your move (row col, e.g., 0 0): ")
                move = tuple(map(int, move.split()))
                while move not in game.available_moves():
                    print("Invalid move. Try again.")
                    move = input("Enter your move (row col, e.g., 0 0): ")
                    move = tuple(map(int, move.split()))
                _, _, _ = game.make_move(move)
            except ValueError:
                print("Invalid input. Please enter row and column numbers separated by a space.")
                continue
        else:  # Agent's turn
            print("Agent's turn...")
            action = agent.choose_action(game.board, game.available_moves())
            _, _, _ = game.make_move(action)

        game.print_board()

    if game.winner:
        if game.winner == "X":
            print("The agent wins! Better luck next time.")
        else:
            print("Congratulations! You win!")
    else:
        print("It's a draw!")

# Main Program
if __name__ == "__main__":
    # Train the Q-learning agent
    trained_agent = train(num_episodes=100000, alpha=0.5, epsilon=0.1, discount_factor=1.0)

    # Play interactively with the trained agent
    play_with_agent(trained_agent)
