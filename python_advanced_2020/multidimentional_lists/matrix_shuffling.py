def read_a_matrix():
    row_count, column_count = [int(x) for x in input().split()]

    matrix = []
    for _ in range(row_count):
        matrix.append([x for x in input().split()])
    return matrix


def command_validator(commands, row_count, col_count):

    is_valid = False
    if len(commands) == 5:
        command = commands[0]
        row1, col1, row2, col2 = [int(x) for x in commands[1:]]
        if command == "swap" and row1 <= row_count >= row2 and col1 <= col_count >= col2:
            is_valid = True
    return is_valid


matrix = read_a_matrix()
new_matrix = None
row_count = len(matrix)
col_count = len(matrix[0])
commands_input = list(input().split(" "))
while commands_input[0] != "END":
    if command_validator(commands_input, row_count, col_count) == True:
        row1, col1, row2, col2 = [int(x) for x in commands_input[1:]]
        first_change = matrix[row2][col2]
        second_change = matrix[row1][col1]
        matrix[row1][col1] = first_change
        matrix[row2][col2] = second_change

        for row in matrix:
            print(' '.join([str(elem) for elem in row]))
    else:
        print("Invalid input!")
    commands_input = list(input().split(" "))












