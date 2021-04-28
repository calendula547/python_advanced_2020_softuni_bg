def multiply(*args):
    multiplication_product = 1
    for x in args:
        multiplication_product *= x
    return multiplication_product


print(multiply(1, -1) == -1)
print(multiply(0, 0) == 0)
print(multiply(1, 1) == 1)
print(multiply(1, -1.7) == -1.7)