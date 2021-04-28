def read_the_matrix():
    row_count = int(input())
    col_count = row_count
    matrix = []
    for _ in range(row_count):
        matrix.append(list(map(int, input().split())))
    return matrix


def primary_diagonal_sum(matrix):
    the_primary_sum = 0
    rows = len(matrix)
    columns = rows
    for row_index in range(rows):
        for col_index in range(columns):
            if row_index == col_index:
                the_primary_sum += matrix[row_index][col_index]
    return the_primary_sum


def secondary_diagonal_sum(matrix):
    the_secondary_sum = 0
    rows = len(matrix)
    columns = rows
    for row_index in range(rows):
        for col_index in range(rows):
            if col_index == rows - row_index - 1:
                the_secondary_sum += matrix[row_index][col_index]
    return the_secondary_sum


matrix = read_the_matrix()
abs_difference = abs(primary_diagonal_sum(matrix) - secondary_diagonal_sum(matrix))
print(abs_difference)


