expression = list(input())
letter_dict = {}
for letter in expression:
    if letter not in letter_dict:
        letter_dict[letter] = 0
    letter_dict[letter] += 1

for key, value in sorted(letter_dict.items()):
    print(f"{key}: {value} time/s")