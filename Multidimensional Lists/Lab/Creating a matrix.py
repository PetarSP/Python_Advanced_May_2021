# CREATING A MATRIX

# Version 1
# n = 5   # num of rows
# m = 6   # num of columns
#
# matrix_of_zeroes = []
#
# for _ in range(n):
#     row = []
#     for _ in range(m):
#         row.append(0)
#     matrix_of_zeroes.append(row)
#
# [print(x) for x in matrix_of_zeroes]

# Version 2

n = 5
m = 6

matrix = [print([0]*m) for _ in range(n)]


