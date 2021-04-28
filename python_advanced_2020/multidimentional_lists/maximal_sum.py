def read_the_matrix():
    rows, cols = [int(x) for x in input().split()]
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, (input().split()))))
    return matrix


def define_submatrix(matrix, row_index, col_index):
    submatrix = []
    for r in range(row_index, row_index + 3):
        row = []
        submatrix.append(row)
        for c in range(col_index, col_index + 3):
            row.append(matrix[r][c])
    return submatrix

def sum_matrix(matrix):
    the_sum = 0

    for row in range(3):
        for col in range(3):
            the_sum += matrix[row][col]
    return the_sum


matrix = read_the_matrix()
row_count = len(matrix)
column_count = len(matrix[0])

if row_count >= 3 and column_count >= 3:
    max_sum = 0
    submatrix_with_max_sum = None
    for r in range(row_count - 2):
        for c in range(column_count - 2):
            current_row = r
            current_col = c
            current_submatrix = define_submatrix(matrix, current_row, current_col)
            submatrix_sum = sum_matrix(current_submatrix)
            if submatrix_sum > max_sum:
                max_sum = submatrix_sum
                submatrix_with_max_sum = current_submatrix

    print(f"Sum = {max_sum}")
    for row in submatrix_with_max_sum:
        print(' '.join([str(elem) for elem in row]))

