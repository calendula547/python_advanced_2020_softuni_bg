num_list = [float(x) for x in input().split()]
round_num = []
[round_num.append(round(num)) for num in num_list]
print(round_num)