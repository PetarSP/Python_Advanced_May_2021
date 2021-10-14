# 1300:1330

def is_in_range(r, c, matrix_size):
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        return True
    return False


size = 8  # square matrix

matrix = [[x for x in input().split()] for _ in range(size)]

# [
# ['.', '.', '.', '.', '.', '.', '.', '.'],
# ['Q', '.', '.', '.', '.', '.', '.', '.'],
# ['.', 'K', '.', '.', '.', 'Q', '.', '.'],
# ['.', '.', '.', 'Q', '.', '.', '.', '.'],
# ['Q', '.', '.', '.', 'Q', '.', '.', '.'],
# ['.', 'Q', '.', '.', '.', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.', 'Q', '.'],
# ['.', 'Q', '.', 'Q', '.', '.', '.', '.']
# ]
queens = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1)
}

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "Q":
            queen_row, queen_col = row, col
            for direction in directions:
                next_row, next_col = queen_row + directions[direction][0], queen_col + directions[direction][1]
                while is_in_range(next_row, next_col, size):

                    if matrix[next_row][next_col] == ".":
                        next_row += directions[direction][0]
                        next_col += directions[direction][1]

                    if not is_in_range(next_row, next_col, size):
                        break

                    if matrix[next_row][next_col] == "Q":
                        break

                    if matrix[next_row][next_col] == "K":
                        queens.append([row, col])
                        break

if queens:
    [print(el) for el in queens]
else:
    print("The king is safe!")
