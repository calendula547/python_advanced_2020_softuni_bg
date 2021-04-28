names = input().split(", ")
result_list = [f"{name} -> {len(name)}" for name in names]
print(", ".join(result_list))

