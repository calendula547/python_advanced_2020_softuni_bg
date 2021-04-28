def read_the_matrix():
    rows_count, columns_count = list(map(int, (input().split())))
    matrix = []
    for _ in range(rows_count):
        matrix.append(list(input().split()))
    return matrix


def find_square_matrix_count(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])
    square_matrix_count = 0
    for r in range(row_count - 1):
        for c in range(col_count - 1):
            current_el = matrix[r][c]
            next_el = matrix[r][c+1]
            down_current_el = matrix[r+1][c]
            down_next_el = matrix[r+1][c+1]
            if current_el == next_el == down_current_el == down_next_el:
                square_matrix_count += 1
    return square_matrix_count


matrix = read_the_matrix()
result = find_square_matrix_count(matrix)
print(result)

