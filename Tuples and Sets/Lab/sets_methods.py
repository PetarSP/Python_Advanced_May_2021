from sqlalchemy import union

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union -> {1, 2, 3, 4, 5, 6}
# c = a | b
# c = a.union(b)

# Intersection -> {3, 4}
# c = a & b
# c = a.intersection(b)

# Subset -> False
# c = a < b
# c = a.issubset(b)

# Difference -> {1, 2}
# c = a - b
# c = a.difference(b)

# Symetrical difference -> {}
# c = a ^ b
# c = a.symmetric_difference(b)


# print(c)
