n, m = [int(i) for i in input().split()]

set_n = {int(input()) for _ in range(n)}
set_m = {int(input()) for _ in range(m)}

[print(i) for i in set_n & set_m]    # intersection -> set_n.intersection(set_m)

