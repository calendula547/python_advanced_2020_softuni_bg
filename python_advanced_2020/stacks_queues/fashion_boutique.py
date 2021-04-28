stack_of_clothes = [int(x) for x in input().split()]
capacity = int(input())
sum_values = 0
racks = 1
while stack_of_clothes:
    current_cloth = stack_of_clothes.pop()
    sum_values += current_cloth
    if sum_values == capacity and len(stack_of_clothes) >= 1:
        racks += 1
        sum_values = 0
    if sum_values > capacity:
        stack_of_clothes.append(current_cloth)
        racks += 1
        sum_values = 0

print(racks)

