def read_a_matrix(n):
    matrix = []
    for r in range(n):
        matrix.append([int(x) for x in input().split()])
    return matrix


def explode(matrix, bomb_row, bomb_column):
    rows_count = len(matrix)
    columns_count = rows_count
    for r in range(rows_count):
        for c in range(columns_count):
            if r == bomb_row and c == bomb_column:
                current_el = matrix[r][c]
                if r+1 < rows_count:
                    if matrix[r+1][c] > 0:
                        matrix[r+1][c] -= current_el
                if r-1 >= 0:
                    if matrix[r-1][c] > 0:
                        matrix[r-1][c] -= current_el
                if c+1 < rows_count:
                    if matrix[r][c+1] > 0:
                        matrix[r][c+1] -= current_el
                if c-1 >= 0:
                    if matrix[r][c-1] > 0:
                        matrix[r][c-1] -= current_el
                if r-1 >= 0 and c+1 < rows_count:
                    if matrix[r-1][c+1] > 0:
                        matrix[r-1][c+1] -= current_el
                if r+1 < rows_count and c-1 >= 0:
                    if matrix[r+1][c-1] > 0:
                        matrix[r+1][c-1] -= current_el
                if r-1 >= 0 and c-1 >= 0:
                    if matrix[r-1][c-1] > 0:
                        matrix[r-1][c-1] -= current_el
                if r+1 < rows_count and c+1 < rows_count:
                    if matrix[r+1][c+1] > 0:
                        matrix[r+1][c+1] -= current_el
                matrix[r][c] = 0
                return matrix


matrix_size = int(input())
matrix = read_a_matrix(matrix_size)
bombs_coordinates = list(input().split(" "))

for b in range(len(bombs_coordinates)):
    row_and_col = bombs_coordinates[b].split(",")
    row_bomb = int(row_and_col[0])
    col_bomb = int(row_and_col[1])

    new_matrix = explode(matrix, row_bomb, col_bomb)
    matrix = new_matrix

alive_cells_count = 0
sum_alive_cells = 0

for r in range(matrix_size):
    for c in range(matrix_size):
        if matrix[r][c] > 0:
            alive_cells_count += 1
            sum_alive_cells += matrix[r][c]

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {sum_alive_cells}")
for r in matrix:
    print(" ".join(str(x) for x in r))
