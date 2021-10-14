def multiply(*args):
    product = 1
    for el in args:
        product *= el
    return product

print(
    multiply(1, 2)
)