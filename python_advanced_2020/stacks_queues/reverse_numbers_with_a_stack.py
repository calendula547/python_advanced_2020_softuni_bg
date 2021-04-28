numbers = input().split()
stack_with_nums = []
for num in range(len(numbers)):
    stack_with_nums.append(numbers.pop())
print(" ".join(stack_with_nums))
