from collections import deque

row_count, col_count = [int(x) for x in input().split()]
text = deque(input())
matrix = []
for r in range(row_count):
    new_row = []
    matrix.append(new_row)
    for col in range(col_count):
        new_row.append(" ")

for r_index in range(row_count):
    for c_index in range(col_count):
        current_el = text.popleft()
        matrix[r_index][c_index] = current_el
        text.append(current_el)

for r_index in range(row_count):
    if r_index % 2 != 0:
        matrix[r_index].reverse()

for row in matrix:
    print("".join([str(el) for el in row]))






