def find_subexpressions(expression):
    opening_brackets = []
    subexpressions = []
    for el in range(len(expression)):
        if expression[el] == "(":
            opening_brackets.append(el)
        elif expression[el] == ")":
            start_index = opening_brackets.pop()
            subexpressions.append(expression[start_index:el+1])
    return subexpressions


for subexpressions in find_subexpressions(input()):
    print(subexpressions)

