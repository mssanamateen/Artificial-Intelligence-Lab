from queue import PriorityQueue

# Define the goal state for the 8-puzzle
#GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)
GOAL_STATE = (1, 2, 3, 8,0,4,7,6,5)

class PuzzleState:
    def __init__(self, board, empty_index, path_cost=0, parent=None):
        self.board = board
        self.empty_index = empty_index  # Index of the empty space (0)
        self.path_cost = path_cost
        self.parent = parent

    def is_goal(self):
        return self.board == GOAL_STATE

    def generate_children(self):
        children = []
        row, col = divmod(self.empty_index, 3)
        directions = {
            "up": (-1, 0), 
            "down": (1, 0), 
            "left": (0, -1), 
            "right": (0, 1)
        }

        for direction, (dr, dc) in directions.items():
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_board = list(self.board)
                new_board[self.empty_index], new_board[new_index] = new_board[new_index], new_board[self.empty_index]
                children.append(PuzzleState(tuple(new_board), new_index, self.path_cost + 1, self))

        return children

    def heuristic(self):
        distance = 0
        for index, value in enumerate(self.board):
            if value != 0:
                goal_index = value - 1
                goal_row, goal_col = divmod(goal_index, 3)
                current_row, current_col = divmod(index, 3)
                distance += abs(goal_row - current_row) + abs(goal_col - current_col)
        return distance

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

def greedy_best_first_search(initial_board):
    initial_index = initial_board.index(0)
    initial_state = PuzzleState(tuple(initial_board), initial_index)

    if initial_state.is_goal():
        return initial_state

    frontier = PriorityQueue()
    frontier.put(initial_state)
    explored = set()

    while not frontier.empty():
        current_state = frontier.get()

        if current_state.is_goal():
            return current_state

        explored.add(current_state.board)

        for child in current_state.generate_children():
            if child.board not in explored:
                frontier.put(child)

    return None  # No solution found

def print_solution(solution):
    path = []
    current_state = solution
    while current_state:
        path.append(current_state.board)
        current_state = current_state.parent
    for state in reversed(path):
        print(state)

# Example usage
initial_board = [2,8,3,1,6,4,7,0,5]  
# Initial configuration initial_board = [1, 2, 3, 4, 5, 6, 0, 7, 8] 
solution = greedy_best_first_search(initial_board)

if solution:
    print("Solution found:")
    print_solution(solution)
else:
    print("No solution found.")
