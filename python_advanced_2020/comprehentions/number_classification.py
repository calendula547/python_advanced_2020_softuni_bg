num_list = [int(num) for num in input().split(", ")]

positive_nums = [f"{num}" for num in num_list if num >= 0]
negative_nums = [f"{num}" for num in num_list if num < 0]
even_nums = [f"{num}" for num in num_list if num % 2 == 0]
odd_nums = [f"{num}" for num in num_list if num % 2 != 0]

print("Positive: " + ", ".join(positive_nums), end="\n")
print("Negative: " + ", ".join(negative_nums), end="\n")
print("Even: " + ", ".join(even_nums), end="\n")
print("Odd: " + ", ".join(odd_nums), end="\n")