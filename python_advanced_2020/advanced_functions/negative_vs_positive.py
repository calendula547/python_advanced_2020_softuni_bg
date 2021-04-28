num_list = [int(x) for x in input().split(" ")]

sum_of_the_negative_nums = sum(list(filter(lambda x: x < 0, num_list)))
sum_of_the_positive_nums = sum(list(filter(lambda x: x > 0, num_list)))
print(sum_of_the_negative_nums)
print(sum_of_the_positive_nums)

if abs(sum_of_the_negative_nums) > sum_of_the_positive_nums:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")