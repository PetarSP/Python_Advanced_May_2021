from collections import deque

expression = deque(list(input()))

stack = []
is_valid = True
valuable_pairs = {
    "{": "}",
    "[": "]",
    "(": ")"
}

for el in expression:
    if el in "{[(":
        stack.append(el)
    else:
        if not stack:
            is_valid = False
            break
        if valuable_pairs[stack.pop()] == el:
            is_valid = True
        else:
            is_valid = False
            break

if is_valid and not stack:
    print("YES")
else:
    print("NO")