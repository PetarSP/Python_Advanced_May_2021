file = "text.txt"

try:
    open(file, "r")
    print("File found")
except FileNotFoundError:
    print("File not found")