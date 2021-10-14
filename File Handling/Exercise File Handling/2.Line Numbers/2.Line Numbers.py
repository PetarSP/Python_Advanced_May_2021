import io
import string

idx = 1

with open("../1.Even Lines/text.txt", "r") as file, open("output.txt", "w") as result:
    while True:
        all_letters_count = 0
        all_punctuation_count = 0
        line = file.readline().strip()
        if not line:
            break
        for each_letter in line:
            if each_letter.isalpha():
                all_letters_count += 1
            if each_letter in string.punctuation:
                all_punctuation_count += 1

        starts_with = f"Line {idx}: "
        line = starts_with + line

        result.write(f"{line} ({all_letters_count})({all_punctuation_count})")
        result.write("\n")
        idx += 1


