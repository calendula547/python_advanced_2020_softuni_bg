matrix_size = int(input())
matrix = [[int(x) for x in input().split(", ")] for i in range(matrix_size)]
first_diagonal = []
second_diagonal = []

for r in range(matrix_size):
    for c in range(matrix_size):
        if r == c:
            first_diagonal.append(matrix[r][c])
        if c == matrix_size - r - 1:
            second_diagonal.append(matrix[r][c])

print(f"First diagonal: {', '.join(str(num) for num in first_diagonal)}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(str(num) for num in second_diagonal)}. Sum: {sum(second_diagonal)}")




