def read_the_matrix():
    row_count = int(input())
    column_count = row_count
    matrix = []
    for _ in range(row_count):
        row = (", ". join(input()))
        matrix.append(row.split(", "))
    return matrix


def find_position(matrix, symbol):
    row_count = len(matrix)

    for row_index in range(row_count):
        for col_index in range(row_count):
            if matrix[row_index][col_index] == symbol:
                result = row_index, col_index
                return result
    return None


matrix = read_the_matrix()
symbol = input()
if find_position(matrix, symbol) is None:
    print(f"{symbol} does not occur in the matrix")
else:
    print(find_position(matrix, symbol))

