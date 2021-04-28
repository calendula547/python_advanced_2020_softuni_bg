n = int(input())
stack_with_nums = []
for _ in range(n):
    query = input().split()

    if query[0] == "1":
        stack_with_nums.append(int(query[1]))
    elif query[0] == "2":
        if stack_with_nums:
            stack_with_nums.pop()
    elif query[0] == "3":
        if stack_with_nums:
            print(max(stack_with_nums))
    elif query[0] == "4":
        if stack_with_nums:
            print(min(stack_with_nums))

stack_with_nums_reversed = reversed(stack_with_nums)

print(', '.join(str(x) for x in stack_with_nums_reversed))

