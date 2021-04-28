def func_executor(*args):
    func_result = []
    for fn in args:
        function = fn[0]
        numbers = fn[1]
        func_result.append(function(*numbers))
    return func_result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))