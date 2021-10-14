def read_matrix():
    n = int(input())

    matrix = []

    for _ in range(n):
        elements = [int(el) for el in input().split(", ")]
        matrix.append(elements)

    return matrix


print([[el for el in row if el % 2 == 0] for row in read_matrix()])
