n = int(input())

odd_set = set()
even_set = set()

for current_row in range(n):
    name = input()
    letters = (sum([ord(letter) for letter in name])) // (current_row + 1)
    if letters % 2 == 0:
        even_set.add(letters)
    else:
        odd_set.add(letters)

sum_odd_set = sum(odd_set)
sum_even_set = sum(even_set)

if sum_even_set == sum_odd_set:
    print(", ".join(str(el) for el in odd_set.union(even_set)))
elif sum_odd_set > sum_even_set:
    print(", ".join(str(el) for el in odd_set.difference(even_set)))
elif sum_odd_set < sum_even_set:
    print(", ".join(str(el) for el in odd_set.symmetric_difference(even_set)))
