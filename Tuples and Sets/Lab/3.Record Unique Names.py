num_names = int(input())

# First way:

# unique_names = set()

# for _ in range(num_names):
#     name = input()
#     unique_names.add(name)
#
# for name in unique_names:
#     print(name)

# Second way:

unique_names = {input() for i in range(num_names)}
[print(name) for name in unique_names]