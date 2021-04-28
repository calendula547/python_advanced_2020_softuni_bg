elements_count_list = list(map(int, input().split()))
first_set = set()
second_set = set()
for i in range(elements_count_list[0]):
    first_set.add(int(input()))
for i in range (elements_count_list[1]):
    second_set.add(int(input()))

union_set = first_set.intersection(second_set)
for num in union_set:
    print(num)
