def read_the_matrix(separator):
    rows_count, columns_count = list(map(int, (input().split(", "))))
    matrix = []
    for _ in range(rows_count):
        matrix.append(list(map(int, (input().split(separator)))))
    return matrix


def get_column_sum(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    column_sums = [0] * columns_count
    for row in range(rows_count):
        for col in range(columns_count):
            column_sums[col] += matrix[row][col]
    return column_sums


matrix = read_the_matrix(" ")
[print(column_sum) for column_sum in get_column_sum(matrix)]

