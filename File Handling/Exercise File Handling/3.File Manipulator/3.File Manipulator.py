import io
import os

command = input().split("-")

while not command[0] == "End":
    instruction = command[0]
    file_name = command[1]
    if instruction == "Create":
        file = open(file_name, "w").close()

    elif instruction == "Add":
        content = command[2]
        with open(file_name, "a") as file:
            file.write(content)
            file.write("\n")

    elif instruction == "Replace":
        old_string = command[2]
        new_string = command[3]
        if os.path.exists(file_name):
            with open(file_name, "r+") as file:
                content = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(content)
        else:
            print("An error occurred")

    elif instruction == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    command = input().split("-")
