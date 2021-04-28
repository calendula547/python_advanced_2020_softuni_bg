only_even_numbers = filter(lambda x: x % 2 == 0, [int(x) for x in input().split()])
print(list(only_even_numbers))