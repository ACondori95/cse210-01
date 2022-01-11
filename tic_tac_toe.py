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

user = True  # when true it refers to x, otherwise o


def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()


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


def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken.")
        return True
    else:
        return False


def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2:
        col = int(col % 3)
    return (row, col)


def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user


def current_user(user):
    if user:
        return "x"
    else:
        return "o"


def iswin(user, board):
    if check_row(user, board):
        return True


def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False


while True:
    active_user = current_user(user)
    print_board(board)
    user_input = input(
        "Please enter a position 1 through 9 or enter 'q' to quit: ")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please try again")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Please try again.")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} won!")
        break

    user = not user
