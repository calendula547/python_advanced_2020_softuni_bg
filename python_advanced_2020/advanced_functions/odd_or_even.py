command = input()
num_list = [int(x) for x in input().split(" ")]
length = len(num_list)

if command == "Odd":
    odd_sum = sum(list(filter(lambda x: x % 2 != 0, num_list)))
    print(odd_sum * length)

if command == "Even":
    even_sum = sum(list(filter(lambda x: x % 2 == 0, num_list)))
    print(even_sum * length)


