sentence = list(input())

opening_brackets_index = []
for index in range(len(sentence)):
    if sentence[index] == "(":
        opening_brackets_index.append(index)
    elif sentence[index] == ")":
        first_index = opening_brackets_index.pop()
        last_index = index
        print("".join(sentence[first_index:last_index + 1]))


