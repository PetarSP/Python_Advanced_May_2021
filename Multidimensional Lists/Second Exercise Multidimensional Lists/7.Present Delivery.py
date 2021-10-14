def is_inside(size, r, c):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def santa_move(direction, r, c, step=1):
    if direction == "up":
        return r - step, c
    if direction == "down":
        return r + step, c
    if direction == "right":
        return r, c + step
    if direction == "left":
        return r, c - step


def houses_around(size, r, c):
    houses = []
    if is_inside(size, r - 1, c):
        houses.append([r - 1, c])
    if is_inside(size, r + 1, c):
        houses.append([r + 1, c])
    if is_inside(size, r, c - 1):
        houses.append([r, c - 1])
    if is_inside(size, r, c + 1):
        houses.append([r, c + 1])
    return houses


number_of_presents = int(input())
size = int(input())

matrix = [[cols for cols in input().split()] for rows in range(size)]

# [
# ['-', 'X', 'V', '-'],
# ['-', 'S', '-', 'V'],
# ['-', '-', '-', '-'],
# ['X', '-', '-', '-']
# ]
santa_row, santa_col = 0, 0
initial_good_kids_count = 0
good_kids_count = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            santa_row, santa_col = row, col
        if matrix[row][col] == "V":
            initial_good_kids_count += 1

good_kids_count = initial_good_kids_count

while True:
    command = input()

    if command == "Christmas morning":
        break

    next_row, next_col = santa_move(command, santa_row, santa_col)

    if matrix[next_row][next_col] == "V":
        number_of_presents -= 1
        good_kids_count -= 1

    elif matrix[next_row][next_col] == "C":
        houses_in_range = houses_around(size, next_row, next_col)
        for house_row, house_col in houses_in_range:
            if matrix[house_row][house_col] == "X":
                number_of_presents -= 1
            if matrix[house_row][house_col] == "V":
                number_of_presents -= 1
                good_kids_count -= 1
            matrix[house_row][house_col] = "-"
            if number_of_presents == 0:
                break
    matrix[santa_row][santa_col] = "-"
    matrix[next_row][next_col] = "S"
    santa_row, santa_col = next_row, next_col

    if number_of_presents == 0:
        break

if good_kids_count > 0 and number_of_presents == 0:
    print("Santa ran out of presents!")
for row in matrix:
    print(' '.join(row))
if good_kids_count == 0:
    print(f"Good job, Santa! {initial_good_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {good_kids_count} nice kid/s.")
