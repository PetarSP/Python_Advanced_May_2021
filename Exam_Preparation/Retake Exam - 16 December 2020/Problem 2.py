def is_in_range(r, c, matrix_size):
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        return True
    return False


initial_str = input()

# square_matrix

size = int(input())
matrix = [[col for col in input()] for row in range(size)]
number_of_turns = int(input())

# [
# ['P', '-', '-', '-'],
# ['M', 'a', 'r', 'k'],
# ['-', 'l', '-', 'y'],
# ['-', '-', 'e', '-']
# ]

player_row, player_col = None, None

player_movement = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "P":
            player_row, player_col = row, col

while not number_of_turns == 0:
    command = input()
    next_player_row, next_player_col = player_row + player_movement[command][0], \
                                       player_col + player_movement[command][1]
    if is_in_range(next_player_row,next_player_col,size):
        if not matrix[next_player_row][next_player_col] == "-":
            initial_str += matrix[next_player_row][next_player_col]
            matrix[next_player_row][next_player_col] = "-"
            matrix[player_row][player_col] = "-"
        matrix[next_player_row][next_player_col] = "P"
        matrix[player_row][player_col] = "-"
        player_row, player_col = next_player_row, next_player_col
    else:
        if initial_str:
            initial_str = initial_str[:-1]
    number_of_turns -= 1

print(initial_str)
for row in matrix:
    print(''.join(str(x)for x in row))