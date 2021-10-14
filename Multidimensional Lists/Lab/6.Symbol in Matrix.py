def read_matrix():
    n = int(input())

    matrix = []

    for _ in range(n):
        row = input()
        matrix.append(row)

    return matrix


matrix = read_matrix()

# [
# ['ABC'],
# ['DEF'],
# ['X!@']
# ]
row, col = None, None
is_symbol = False
symbol = input()

for r in range(len(matrix)):
    if is_symbol:
        break
        
    for c in range(len(matrix[r])):
        if matrix[r][c] == symbol:
            is_symbol = True
            row, col = r, c
            break

if is_symbol:
    print(f"({row}, {col})")
else:
    print(f"{symbol} does not occur in the matrix")