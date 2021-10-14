# Variant 1

# def age_assignment(*args, **kwargs):
#     some_dict = {}
#     for key, value in kwargs.items():
#         for name in args:
#             if name[0] == key:
#                 some_dict[name] = value
#     return some_dict

# Variant 2

# def age_assignment(*args, **kwargs):
#     result = {}
#     for name in args:
#         abr = name[0]
#         result[name] = kwargs[abr]
#     return result

# Variant 3

def age_assignment(*args, **kwargs):
    return {x: kwargs[x[0]] for x in args}


print(age_assignment("Peter", "George", G=26, P=19))


