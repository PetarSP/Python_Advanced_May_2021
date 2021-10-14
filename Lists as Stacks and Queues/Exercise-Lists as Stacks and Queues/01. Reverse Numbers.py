str_as_list = [int(num) for num in input().split()]
stack = []
while str_as_list:
    stack.append(str_as_list.pop())
print(*stack)