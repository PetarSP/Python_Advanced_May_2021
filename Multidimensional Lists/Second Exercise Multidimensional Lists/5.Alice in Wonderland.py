def is_inside(field_size, r, c):
    if 0 <= r < field_size and 0 <= c < field_size:
        return True
    return False


def get_next_psn(command, alice_row, alice_col):
    if command == "up":
        return alice_row - 1, alice_col
    if command == "down":
        return alice_row + 1, alice_col
    if command == "right":
        return alice_row, alice_col + 1
    if command == "left":
        return alice_row, alice_col - 1


size = int(input())

territory = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]

# [
# ['.', 'A', '.', '.', 1],
# ['R', '.', 2, '.', '.'],
# [4, 7, '.', 1, '.'],
# ['.', '.', '.', 2, '.'],
# ['.', 3, '.', '.', '.']
# ]
alice_row, alice_col = 0, 0
for row in range(size):
    for col in range(size):
        if territory[row][col] == "A":
            alice_row, alice_col = row, col

bags_of_tea = 0
territory[alice_row][alice_col] = "*"
while True:
    command = input()
    alice_row, alice_col = get_next_psn(command, alice_row, alice_col)
    if not is_inside(size, alice_row, alice_col):
        break

    cell_value = territory[alice_row][alice_col]
    territory[alice_row][alice_col] = "*"

    if cell_value == "R":
        break

    if str(cell_value).isdigit():
        bags_of_tea += cell_value
        if bags_of_tea >= 10:
            break

if bags_of_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in territory:
    print(" ".join(str(x) for x in row))
