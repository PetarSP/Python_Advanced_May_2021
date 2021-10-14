def read_matrix():
    n, m = [int(x) for x in input().split(", ")]

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(", ")]  # check this split !
        matrix.append(row)

    return matrix


matrix = read_matrix()

# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0

n = len(matrix)
m = len(matrix[0])

all_2_x_2_matrix_sum_indices = []

for r in range(n - 1):
    for c in range(m - 1):
        current_sum = sum([
            matrix[r][c],
            matrix[r][c + 1],
            matrix[r + 1][c],
            matrix[r + 1][c + 1],
        ])
        all_2_x_2_matrix_sum_indices.append(
            (current_sum,
             r,
             c)
        )
max_sum = 0
row_idx, col_idx = None, None
for matrix_sum, row, col in all_2_x_2_matrix_sum_indices:
    if max_sum < matrix_sum:
        max_sum = matrix_sum
        row_idx = row
        col_idx = col

print(matrix[row_idx][col_idx],
      matrix[row_idx][col_idx + 1])
print(matrix[row_idx + 1][col_idx],
      matrix[row_idx + 1][col_idx + 1])
print(max_sum)
