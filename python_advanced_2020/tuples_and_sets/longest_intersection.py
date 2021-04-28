n = int(input())


def find_intervals(interval):
    set_with_nums = set()
    start_digit = int(interval[0])
    end_digit = int(interval[1])
    digit = start_digit
    for i in range(end_digit+1 - start_digit):
        set_with_nums.add(digit)
        digit += 1
    return set_with_nums


intervals = []
[intervals.append(input().split("-")) for _ in range(n)]
max_length = 0
max_intersection = None

for interval in intervals:
    first_interval = interval[0].split(",")
    first_set = find_intervals(first_interval)

    second_interval = interval[1].split(",")
    second_set = find_intervals(second_interval)

    current_intersection_set = first_set.intersection(second_set)
    current_length = len(current_intersection_set)
    if current_length > max_length:
        max_intersection = current_intersection_set
        max_length = current_length

print(f"Longest intersection is {list(max_intersection)} with length {max_length}")


