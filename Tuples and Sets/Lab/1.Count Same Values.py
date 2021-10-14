numbers = input().split()

num_dict = {}

for num in numbers:
    if num not in num_dict:
        num_dict[num] = 1
    else:
        num_dict[num] += 1

for key, value in num_dict.items():
    print(f"{float(key)} - {value} times")