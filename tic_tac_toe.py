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
    if user_input.lower() == 'q':
        print("Thanks for playing")
        return True
    else:
        return False


def check_input(user_input):
    # check if it is a nummber
    if not isnum(user_input):
        return False
    user_input = int(user_input)
    # check if it is 1-9
    if not bounds(user_input):
        return False
    return True


def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of bounds")
        return False
    else:
        return True


def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else:
        return True


while True:
    print_board(board)
    user_input = input(
        "Please enter a position 1 through 9 or enter 'q' to quit: ")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please try again")
        continue
