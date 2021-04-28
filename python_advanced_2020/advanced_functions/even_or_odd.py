def even_odd(*args):
    if args[-1] == "even":
        even_nums = list(filter(lambda x: x % 2 == 0, args[:-1]))
        return even_nums
    if args[-1] == "odd":
        odd_nums = list(filter(lambda x: x % 2 != 0, args[:-1]))
        return odd_nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))