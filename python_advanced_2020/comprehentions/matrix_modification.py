matrix_size = int(input())
matrix = [[int(x) for x in input().split()] for i in range(matrix_size)]

while True:
    commands = input().split()
    command = commands[0]
    if command == "END":
        break
    row_given = int(commands[1])
    col_given = int(commands[2])
    value = int(commands[3])
    if row_given < 0 or row_given >= matrix_size or col_given < 0 or col_given >= matrix_size:
        print("Invalid coordinates")

    elif command == "Add":
        for r in range(matrix_size):
            for c in range(matrix_size):
                if r == row_given and c == col_given:
                    matrix[r][c] += value
    elif command == "Subtract":
        for r in range(matrix_size):
            for c in range(matrix_size):
                if r == row_given and c == col_given:
                    matrix[r][c] -= value

[print(" ".join(str(x) for x in row)) for row in matrix]