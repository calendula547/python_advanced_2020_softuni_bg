def read_the_matrix():
    row_count, column_count = list(map(int, input().split(", ")))
    matrix = []
    for _ in range(row_count):
        matrix.append([])
        row = list(map(int, input().split(", ")))
        for value in row:
            matrix[-1].append(value)
    return matrix


def sum_matrix(matrix):
    the_sum = 0
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    for row in range(rows_count):
        for col in range(columns_count):
            the_sum += matrix[row][col]
    return the_sum


matrix = read_the_matrix()
print(sum_matrix(matrix))
print(matrix)