# errors

class InvalidPsn(Exception):
    pass


# var
turn = 1

psn_dict = {
    "1": (0, 0),
    "2": (0, 1),
    "3": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (2, 0),
    "8": (2, 1),
    "9": (2, 2)
}


# read the player - assign sign to the player
def read_player():
    player_one = input("Player one name: ")
    player_two = input("Player two name: ")
    while True:
        player_one_sign = input(f"{player_one} would like to play with 'X' or 'O'? ").upper()
        if not player_one_sign == "X" and not player_one_sign == "O":
            continue
        else:
            player_two_sign = "O" if player_one_sign == "X" else "X"
        player_one = [player_one, player_one_sign]
        player_two = [player_two, player_two_sign]
        return player_one, player_two


# numeration of the board
def board_numeration():
    print("This is numeration of the board:")
    n = 3
    m = 3
    matrix = []
    el = 0
    for row in range(n):
        inner_list = []
        for col in range(m):
            el += 1
            inner_list.append(el)
        matrix.append(inner_list)
    matrix = [[f"|  {el} " for el in row] for row in matrix]
    for row in matrix:
        print(*row, end=" |" + "\n")
    print(f"{player_one[0]} starts first!")


# matrix
board = [[" " for col in range(3)] for row in range(3)]


def print_board(board):
    for row in board:
        print(row)


# current player turn
def current_player(turn):
    if turn % 2 == 1:
        return player_one
    return player_two


# player choice

def player_choice(current_player):
    player_input = input(f"{current_player} choose a free position [1-9]:")
    if player_input in psn_dict:
        player_choice_coord = psn_dict[player_input]
        return player_choice_coord


# check if psn is free
def is_psn_free(board, player_choice):
    player_r, player_c = player_row, player_col
    if board[player_r][player_c] == " ":
        return True
    return False


# wining conditions

def is_winning(board):
    # horizontal
    win = False
    all([el for x in len(board)])
    # vertical
    # primary_diagonal
    # secondary_diagonal

# -------------------------------------------------

player_one, player_two = read_player()
board_numeration()

while True:
    current_player(turn)
    player_row, player_col = player_choice(current_player(turn))

    if not is_psn_free(board, player_choice):
        print("Psn not valid!")
        continue

    board[player_row][player_col] = current_player(turn)[1]

    print_board(board)

    turn += 1
# -------------------------------------------------
