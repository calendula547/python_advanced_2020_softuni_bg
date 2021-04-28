def read_the_matrix():
    size_of_matrix = int(input())
    matrix = []
    for _ in range(size_of_matrix):
        matrix.append(list(map(int, (input().split()))))
    return matrix


def sum_primary_diagonal(matrix):
    sum_of_diagonal = 0
    row_count = len(matrix)
    column_count = row_count
    for row_index in range(row_count):
        for cow_index in range(column_count):
            if row_index == cow_index:
                sum_of_diagonal += matrix[row_index][cow_index]
    return sum_of_diagonal


matrix = read_the_matrix()
print(sum_primary_diagonal(matrix))

