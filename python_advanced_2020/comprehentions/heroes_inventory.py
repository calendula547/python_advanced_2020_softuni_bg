heroes_dict = {name: {} for name in input().split(", ")}

while True:
    name_item_cost = input().split("-")
    name = name_item_cost[0]
    if name == "End":
        break
    item = name_item_cost[1]
    cost = int(name_item_cost[2])
    if item not in heroes_dict[name]:
        heroes_dict[name][item] = cost

[print(f"{name} -> Items: {len(heroes_dict[name])}, Cost: {sum(heroes_dict[name].values())}") for name in heroes_dict.keys()]

