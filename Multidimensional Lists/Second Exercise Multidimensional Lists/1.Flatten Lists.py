# 1 2 3 |4 5 6 |  7  88

# 7 88 4 5 6 1 2 3

sublists = input().split("|")
result = []
matrix = [x.split() for x in sublists]
for x in range(len(matrix) - 1, -1, -1):
    result += matrix[x]

print(" ".join(result))
