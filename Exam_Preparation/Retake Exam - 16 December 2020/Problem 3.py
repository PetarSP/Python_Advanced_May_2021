# [
# [1],              0
# [1, 1],           1
# [1, 2, 1],        2
# [1, 3, 3, 1],     3
# [1, 4, 6, 4, 1]]  4
#  0  1  2  3  4

def get_magic_triangle(n: int):
    triangle = [[1], [1, 1]]
    for row in range(2, n):
        triangle.append([])
        triangle[-1].append(1)
        for col in range(1, row):
            next_list = triangle[row - 1][col - 1] + triangle[row - 1][col]
            triangle[-1].append(next_list)
        triangle[-1].append(1)
    return triangle


print(get_magic_triangle(5))
