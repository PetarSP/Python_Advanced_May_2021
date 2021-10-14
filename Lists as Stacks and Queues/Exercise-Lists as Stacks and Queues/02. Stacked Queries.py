# Function to push the num(int) into the stack
def push_to_the_stack():
    stack.append(int(command[1]))


# Function to delete the num at the top of the stack
def pop_from_the_stack():
    if stack:
        stack.pop()


# Function to print the max num in the stack
def max_num(stack: list):
    print(max(stack))


# Function to print the min num in the stack
def min_num(stack: list):
    print(min(stack))


number_of_input = int(input())

stack = []
while number_of_input:
    command = input().split()
    if command[0] == "1":
        push_to_the_stack()
    elif command[0] == "2":
        pop_from_the_stack()
    elif command[0] == "3":
        if stack:
            max_num(stack)
    elif command[0] == "4":
        if stack:
            min_num(stack)
    number_of_input -= 1

stack = [str(i) for i in stack]
print(", ".join(stack[::-1]))