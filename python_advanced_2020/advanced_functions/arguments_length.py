def args_length(*args):
    length = len(args)
    return length


print(args_length(1, 32, 5))
print(args_length("john", "peter"))