def get_value(matrix, size, r, c):
    if not is_in_range(r, c, size):
        return 0
    if matrix[r][c] == "D":
        corresponding_coord = matrix[r][0] + matrix[r][-1] + matrix[0][c] + matrix[-1][c]
        doubled_value = corresponding_coord * 2
        return doubled_value
    elif matrix[r][c] == "T":
        corresponding_coord = matrix[r][0] + matrix[r][-1] + matrix[0][c] + matrix[-1][c]
        tripled_coord = corresponding_coord * 3
        return tripled_coord
    elif matrix[r][c] == "B":
        return 510
    else:
        value = matrix[r][c]
        return value


def get_turn():
    turn_str = input()
    vals = turn_str[1:-1].split(", ")
    return [int(val) for val in vals]


def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


first_player, second_player = input().split(", ")
# square matrix
size = 7
matrix = [[int(el) if el.isdigit() else str(el) for el in input().split()] for rows in range(size)]

# [0    1    2    3    4    5     6
# [12, 21,  18,   4,  20,   7,   11], 0
# [ 9, 'D', 'D', 'D', 'D', 'D',  10], 1
# [15, 'D', 'T', 'T', 'T', 'D',   3], 2
# [ 2, 'D', 'T', 'B', 'T', 'D',  19], 3
# [17, 'D', 'T', 'T', 'T', 'D',   6], 4
# [22, 'D', 'D', 'D', 'D', 'D',  14], 5
# [ 5,  8,  23,  13,   16,   1,  24]  6
# ]

current_player = [first_player, 501, 0]
other_player = [second_player, 501, 0]

while True:
    current_throw_row, current_throw_col = get_turn()
    if not is_in_range(current_throw_row, current_throw_col, size):
        current_player[2] += 1
        current_player, other_player = other_player, current_player
        continue
    else:
        current_player[1] -= get_value(matrix, size, current_throw_row, current_throw_col)
        current_player[2] += 1

    if current_player[1] <= 0:
        print(f"{current_player[0]} won the game with {current_player[2]} throws!")
        break
    current_player, other_player = other_player, current_player
