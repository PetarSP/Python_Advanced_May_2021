from collections import deque

parentheses = deque(list(input()))

stack = []
valuable_pairs = "(){}[]"
is_balanced = True

for el in parentheses:
    if el in "([{":
        stack.append(el)
    else:
        if not stack:
            is_balanced = False
            break
        last_el = stack.pop()
        pair = f"{last_el}{el}"
        if pair in valuable_pairs:
            continue
        else:
            is_balanced = False
            break
if is_balanced:
    print("YES")
else:
    print("NO")
