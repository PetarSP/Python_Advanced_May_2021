text = list(input())

def permutation(index, values):
    if index == len(values):
        print("".join(values))
        return
    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        permutation(index + 1, values)
        values[i], values[index] = values[index], values[i]


permutation(0, text)
