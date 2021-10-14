n, m = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(n):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

sum_of_el = 0

for rows in matrix:
    for el in rows:
        sum_of_el += el


print(sum_of_el)
print(matrix)
