def numbers_searching(*args):
    list_of_args = list(args)
    missing_el = 0
    list_of_duplicates = []
    min_number = min(list_of_args)
    max_num = max(list_of_args)
    for el in range(min_number, max_num + 1):
        if el not in list_of_args:
            missing_el = el
    for el in list_of_args:
        number_of_appearance = list_of_args.count(el)
        if number_of_appearance > 1 and el not in list_of_duplicates:
            list_of_duplicates.append(el)
    return [missing_el, sorted(list_of_duplicates)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))