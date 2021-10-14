n, m = [int(x) for x in input().split()]
matrix = [input().split() for x in range(n)]

# [
# ['A', 'B', 'B', 'D'],
# ['E', 'B', 'B', 'B'],
# ['I', 'J', 'B', 'B']
# ]
found_2x2_matrix = 0

for row in range(n - 1):
    for col in range(m - 1):
        if matrix[row][col] == \
                matrix[row][col + 1] == \
                matrix[row + 1][col] == \
                matrix[row + 1][col + 1]:
            found_2x2_matrix += 1
print(found_2x2_matrix)