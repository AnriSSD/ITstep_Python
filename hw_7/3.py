def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Nimushi
n = 5
factorial_of_n = factorial(n)
print(factorial_of_n)
