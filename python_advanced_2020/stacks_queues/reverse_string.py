def reverse_string(text):
    stack_text = []
    [stack_text.append(x) for x in text]
    reversed_text = []
    for i in range(len(stack_text)):
        reversed_text.append(stack_text.pop())

    return "".join(reversed_text)


print(reverse_string(input()))