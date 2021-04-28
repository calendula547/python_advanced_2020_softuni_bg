category_dict = {category: {} for category in input().split(", ")}
n = int(input())

for i in range(n):
    line = input().split(" - ")
    category = line[0]
    item = line[1]
    q_and_q = line[2].split(";")
    quantity = int(q_and_q[0].split(":")[1])
    quality = int(q_and_q[1].split(":")[1])
    category_dict[category][item] = (quantity, quality)

count_items = 0
for category, item in category_dict.items():
    for key in item:
        count_items += item[key][0]

quality_sum = 0
for category, item in category_dict.items():
    for key in item:
        quality_sum += item[key][1]

print(f"Count of items: {count_items}")
print(f"Average quality: {quality_sum/len(category_dict):.2f}")
[print(f"{key} -> {', '.join(category_dict[key].keys())}") for key in category_dict.keys()]