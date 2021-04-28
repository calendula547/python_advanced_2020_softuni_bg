n_lines = int(input())
odd_nums = set()
even_nums = set()

for i in range(1, n_lines+1):
    sum_of_chars = 0
    name = input()
    for ch in name:
        sum_of_chars += ord(ch)
    devised_sum = int(sum_of_chars / i)
    if devised_sum % 2 == 0:
        even_nums.add(devised_sum)
    else:
        odd_nums.add(devised_sum)

even_sum = sum(even_nums)
odd_sum = sum(odd_nums)

if even_sum == odd_sum:
    union_set = odd_nums.union(even_nums)
    print(str(union_set)[1:-1])
elif even_sum > odd_sum:
    symmetric_diff_set = odd_nums.symmetric_difference(even_nums)
    print(str(symmetric_diff_set)[1:-1])
else:
    diff_set = odd_nums.difference(even_nums)
    print(str(diff_set)[1:-1])




