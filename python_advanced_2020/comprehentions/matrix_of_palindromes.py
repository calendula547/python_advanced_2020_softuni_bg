row_count, column_count = [int(num) for num in input().split()]
matrix = []
for r_index in range(97, 97 + row_count):
    row = [f"{chr(r_index)}{chr(r_index + col)}{chr(r_index)}" for col in range(column_count)]
    matrix.append(row)
[print(" ".join(row)) for row in matrix]
