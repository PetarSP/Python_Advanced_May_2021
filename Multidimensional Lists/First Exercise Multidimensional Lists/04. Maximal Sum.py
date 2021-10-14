n, m = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(n)]

# [
# [1, 5, 5, 2, 4],
# [2, 1, 4, 14, 3],
# [3, 7, 11, 2, 8],
# [4, 8, 12, 16, 4]
# ]

all_matrix_sum = []

for row in range(n - 2):
    for col in range(m - 2):
        matrix_3x3_sum = matrix[row][col] + \
                         matrix[row][col + 1] + \
                         matrix[row][col + 2] + \
                         matrix[row + 1][col] + \
                         matrix[row + 1][col + 1] + \
                         matrix[row + 1][col + 2] + \
                         matrix[row + 2][col] + \
                         matrix[row + 2][col + 1] + \
                         matrix[row + 2][col + 2]
        all_matrix_sum.append((matrix_3x3_sum, row, col))

biggest_matrix = max(all_matrix_sum)
biggest_sum = max(all_matrix_sum)[0]
print(f"Sum = {biggest_sum}")
max_matrix_row, max_matrix_col = biggest_matrix[1], biggest_matrix[2]
print(matrix[max_matrix_row][max_matrix_col],
      matrix[max_matrix_row][max_matrix_col + 1],
      matrix[max_matrix_row][max_matrix_col + 2])
print(matrix[max_matrix_row + 1][max_matrix_col],
      matrix[max_matrix_row + 1][max_matrix_col + 1],
      matrix[max_matrix_row + 1][max_matrix_col + 2])
print(matrix[max_matrix_row + 2][max_matrix_col],
      matrix[max_matrix_row + 2][max_matrix_col + 1],
      matrix[max_matrix_row + 2][max_matrix_col + 2])
