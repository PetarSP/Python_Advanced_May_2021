try:
    text = input()
    times_to_repeat = int(input())
    multiply_text = text * times_to_repeat
    print(multiply_text)
except ValueError:
    print("Variable times must be an integer")
