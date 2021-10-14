# f(n) = f(n-1) * n
# f(0) = 1
# f(1) = 1

def factorial(n):
    print(f"Calculating f({n})")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(
    factorial(10)
)