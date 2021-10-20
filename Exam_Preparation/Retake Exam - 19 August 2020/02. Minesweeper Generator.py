# square matrix
def is_in_range(r, c, matrix_size):
    if 0 <= r < matrix_size and 0 <= c < matrix_size and matrix[r][c] != "*":
        return True
    return False


def bomb_psn():
    bomb_row, bomb_col = [int(x) for x in input()[1:][:-1].split(', ')]
    return bomb_row, bomb_col


size = int(input())
bombs = int(input())

matrix = [[0 for col in range(size)] for row in range(size)]

bomb_spread = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
    "up_left": (-1, -1),
    "up_right": (-1, +1),
    "down_left": (+1, -1),
    "down_right": (+1, +1)
}

# [None, None, None, '*']
# [None, '*', None, None]
# [None, None, '*', None]
# ['*', None, None, None]

while not bombs == 0:
    bomb_row, bomb_col = bomb_psn()
    matrix[bomb_row][bomb_col] = "*"
    for key, value in bomb_spread.items():
        next_bomb_row, next_bomb_col = bomb_row + bomb_spread[key][0], bomb_col + bomb_spread[key][1]
        if not is_in_range(next_bomb_row, next_bomb_col, size):
            continue
        matrix[next_bomb_row][next_bomb_col] += 1
    bombs -= 1

# [
# [1, 1, 2, '*'],
# [1, '*', 3, 2],
# [2, 3, '*', 1],
# ['*', 2, 1, 1]
# ]
matrix_as_str = [[str(y) for y in x] for x in matrix]
[print(' '.join(x)) for x in matrix_as_str]
