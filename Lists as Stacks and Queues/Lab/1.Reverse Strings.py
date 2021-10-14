# Have to use a stack

word = list(input())

reversed_word = []

while word:
    popped_el = word.pop()
    reversed_word.append(popped_el)

print("".join(reversed_word))
