def if_parentheses_is_balanced(expression):
    #expression_without_intervals = expression.replace(" ", "")
    list_of_symbols = list(expression)
    opening_brackets_stack = []
    is_balanced = False
    for i in range(len(list_of_symbols)):
        symbol = list_of_symbols[i]
        if symbol == "(" or symbol == "[" or symbol == "{":
            opening_brackets_stack.append(list_of_symbols[i])
        else:
            if opening_brackets_stack:
                last_add_el = opening_brackets_stack.pop()
                if symbol == ")" and last_add_el == "(" or \
                    symbol == "]" and last_add_el == "[" or \
                    symbol == "}" and last_add_el == "{" or \
                    symbol == " " and last_add_el == " ":
                    is_balanced = True

                else:
                    break

    if is_balanced == True:
        print("YES")
    else:
        print("NO")



parentheses_exp = input()
if_parentheses_is_balanced(parentheses_exp)