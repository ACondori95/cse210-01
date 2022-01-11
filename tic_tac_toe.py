# tic tac toe

"""
tic tac toe board
[
  [-, -, -],
  [-, -, -],
  [-, -, -]
]

user_input -> something 1-9
if they enter anything else: tell them to go again
check if the user_input is already taken
add itto the board
check if user won: checking rows, columns and diagonals
toggle between users upon successful moves
"""

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]


def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()


print_board(board)


def quit(user_input):
    if user_input == 'q':
        print("Thanks for playing")
        return True
    else:
        return False


while True:
    user_input = input(
        "Please enter a position 1 through 9 or enter 'q' to quit: ")
