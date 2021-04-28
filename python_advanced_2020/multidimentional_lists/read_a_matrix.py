def read_the_matrix():
    rows_count, columns_count = map(int, input().split(", "))
    matrix = []
    for _ in range(rows_count):
        matrix.append(list(map(int, (input().split(", ")))))
    return matrix


print(read_the_matrix())


def read_a_matrix():
    matrix_size = int(input())
    matrix = [[int(x) for x in input().split(", ")] for i in range(matrix_size)]
    print(matrix)